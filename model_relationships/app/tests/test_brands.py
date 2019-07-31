# # CORRECT THE VALUES!!!

# import json

# def test_get_no_bands(client):
#     res = client.get("/bands")
#     assert res.status_code == 200
#     assert json.loads(res.data.decode()) == []

# def test_create_band(client):
#     res = client.post("/bands", data={"name": "The Stooges"})
#     assert res.status_code == 200

# def test_sample_band(sample_band):
#     assert sample_band.id == 1
#     assert sample_band.name == "The Stooges"

# def test_get_band_by_id(client, sample_band):
#     res = client.get(f"/bands/{sample_band.id}")
#     band_dict = json.loads(res.data.decode())
#     assert band_dict["name"] == "The Stooges"

# def test_create_band_and_check(client):
#     client.post("/bands", data={"name": "The Stooges"})
#     res = client.get("/bands")
#     bands = json.loads(res.data.decode())
#     assert len(bands) == 1
#     assert bands[0]["name"] == "The Stooges"

# def test_create_band_and_fetch(client, sample_band):
#     res = client.get(f"/bands/{sample_band.id}")
#     assert res.status_code == 200

#     band_dict = json.loads(res.data.decode())
#     assert band_dict["name"] == "The Stooges"

# def test_update_band(client, sample_band):
#     res = client.put(f"/bands/{sample_band.id}", data={"name": "Not The Stooges"})
#     assert res.status_code == 200
#     assert json.loads(res.data.decode()) == sample_band.id

#     res = client.get(f"/bands/{sample_band.id}")
#     band_dict = json.loads(res.data.decode())
#     assert band_dict["name"] == "Not The Stooges"

# def test_get_band_with_artists(client, sample_artist):
#     res = client.get(f"/bands/{sample_artist.band_id}")
#     band_dict = json.loads(res.data.decode())
#     assert band_dict["artists"][0]["name"] == "Iggy Pop"

# def test_delete_band(client, sample_band):
#     res = client.delete(f"/bands/{sample_band.id}")
#     assert res.status_code == 200

# # This is ridiculous
# def test_get_band_by_name(client, sample_band):
#     res = client.get("/bands/The Stooges")
#     assert res.status_code == 200

#     band_dict = json.loads(res.data.decode())
#     assert band_dict["name"] == "The Stooges"
