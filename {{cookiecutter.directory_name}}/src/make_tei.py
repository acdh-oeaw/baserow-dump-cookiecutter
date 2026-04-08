import json
import shutil
import glob
import lxml.etree as ET
import os
from datetime import date

from acdh_baserow_pyutils import get_related_table_info
from acdh_tei_pyutils.tei import TeiReader

from tqdm import tqdm

from config import JSON_FOLDER, TEI_FOLDER, br_client, BASEROW_DB_ID


files = sorted(glob.glob(f"{JSON_FOLDER}/*.json"))
shutil.rmtree(TEI_FOLDER, ignore_errors=True)
os.makedirs(TEI_FOLDER, exist_ok=True)


db_dict = br_client.fetch_table_field_dict(BASEROW_DB_ID)
current_day = str(date.today())


for x in tqdm(files, total=len(files)):
    doc = TeiReader("tei-template.xml")
    _, tail = os.path.split(x)
    tei_file_name = tail.replace(".json", ".xml")
    table_name = tail.replace(".json", "")
    table_dict = db_dict[table_name]
    table_id = f"{table_dict['id']}"
    tei_save_path = os.path.join(TEI_FOLDER, tei_file_name)
    tei_body = doc.any_xpath(".//tei:body")[0]
    tei_title_main = doc.any_xpath(".//tei:title[@type='main']")[0]
    tei_title_main.text = f"data dump from baserow table '{table_name}'"
    name_node = doc.any_xpath(".//tei:name[@xml:id]")[0]
    name_node.text = table_name
    idno_node = doc.any_xpath(".//tei:idno")[0]
    idno_node.text = table_id
    date_node = doc.any_xpath(".//tei:date")[0]
    date_node.attrib["when-iso"] = current_day
    with open(x, "r", encoding="utf-8") as fp:
        data = json.load(fp)
    table_node = ET.Element("{http://www.tei-c.org/ns/1.0}table")
    first_item = list(data[list(data.keys())[0]].keys())
    table_node.attrib["rows"] = f"{len(data)}"
    table_node.attrib["cols"] = f"{len(first_item)}"
    th_row = ET.Element("{http://www.tei-c.org/ns/1.0}row")
    th_row.attrib["role"] = "label"
    table_node.append(th_row)
    for th in first_item:
        th_cell = ET.Element("{http://www.tei-c.org/ns/1.0}cell")
        th_cell.attrib["role"] = "label"
        th_cell.text = th
        th_row.append(th_cell)
    for _, tr in data.items():
        tr_node = ET.Element("{http://www.tei-c.org/ns/1.0}row")
        tr_node.attrib["role"] = "data"
        table_node.append(tr_node)
        for key, value in tr.items():
            td_cell = ET.Element("{http://www.tei-c.org/ns/1.0}cell")
            td_cell.attrib["role"] = "data"
            if isinstance(value, (str, int, float)):
                td_cell.text = f"{value}"
            if isinstance(value, list):
                td_cell = ET.Element("{http://www.tei-c.org/ns/1.0}cell")
                for item in value:
                    rs = ET.Element("{http://www.tei-c.org/ns/1.0}rs")
                    related_table_id, related_table_name = get_related_table_info(
                        table_name, key, db_dict
                    )
                    rs.attrib[
                        "ref"
                    ] = f"#{related_table_name}__{related_table_id}__{item['id']}"
                    rs.attrib["type"] = f"{related_table_name}"
                    rs.text = f"{item['value']}"
                    td_cell.append(rs)
            tr_node.append(td_cell)
    tei_body.append(table_node)
    doc.tree_to_file(tei_save_path)
