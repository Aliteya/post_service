def test_get_all_posts(authorized_client, test_posts):
    response = authorized_client.post("/posts/")
    assert response.status_code == 200

# def test():
#     pass

# def test():
#     pass

# def test():
#     pass

# def test():
#     pass