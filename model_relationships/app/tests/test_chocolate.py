import json

def test_get_no_brands(client):
    res = client.get("/brands")
    assert res.status_code == 200
    assert json.loads(res.data.decode()) == []

def test_sample_brand_fixture(sample_brand):
    assert sample_brand.id == 1
    assert sample_brand.name == "Kit Kat"

def test_solo_brand_fixture(solo_artist):
    assert sample_brand2.id == 1
    assert sample_brand2.name == "Lindt"

def test_create_brand_with_band(client, sample_band):
    brand_info = {"name": "Kit Kat", "band": sample_band.id}
    res = client.post("/brands", data=brand_info)
    assert res.status_code == 200

def test_create_solo_brand(client):
    brand_info = {"name": "Lindt"}
    res = client.post("/brands", data=brand_info)
    assert res.status_code == 200

    res = client.get("/brands")
    brands = json.loads(res.data.decode())
    assert len(brands) == 1
    assert brands[0]['name'] == "Lindt"
    assert brands[0].get('band') is None

def test_get_one_brand(client, sample_brand):
    res = client.get(f"/brands/{sample_brand.id}")
    brand_dict = json.loads(res.data.decode())
    assert brand_dict["name"] == "Kit Kat"