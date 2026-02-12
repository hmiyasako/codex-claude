def test_create_todo(client):
    response = client.post("/todos", json={"title": "Buy milk"})
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Buy milk"
    assert data["completed"] is False
    assert "id" in data
    assert "created_at" in data
    assert "updated_at" in data


def test_list_todos(client):
    client.post("/todos", json={"title": "Task 1"})
    client.post("/todos", json={"title": "Task 2"})
    response = client.get("/todos")
    assert response.status_code == 200
    assert len(response.json()) == 2


def test_get_todo(client):
    create = client.post("/todos", json={"title": "Read book"})
    todo_id = create.json()["id"]
    response = client.get(f"/todos/{todo_id}")
    assert response.status_code == 200
    assert response.json()["title"] == "Read book"


def test_get_todo_not_found(client):
    response = client.get("/todos/9999")
    assert response.status_code == 404


def test_update_todo_title(client):
    create = client.post("/todos", json={"title": "Old title"})
    todo_id = create.json()["id"]
    response = client.patch(f"/todos/{todo_id}", json={"title": "New title"})
    assert response.status_code == 200
    assert response.json()["title"] == "New title"


def test_update_todo_completed(client):
    create = client.post("/todos", json={"title": "Do laundry"})
    todo_id = create.json()["id"]
    response = client.patch(f"/todos/{todo_id}", json={"completed": True})
    assert response.status_code == 200
    assert response.json()["completed"] is True


def test_update_todo_not_found(client):
    response = client.patch("/todos/9999", json={"title": "Nope"})
    assert response.status_code == 404


def test_delete_todo(client):
    create = client.post("/todos", json={"title": "Throw away"})
    todo_id = create.json()["id"]
    response = client.delete(f"/todos/{todo_id}")
    assert response.status_code == 204
    get_response = client.get(f"/todos/{todo_id}")
    assert get_response.status_code == 404


def test_delete_todo_not_found(client):
    response = client.delete("/todos/9999")
    assert response.status_code == 404


def test_create_todo_empty_title(client):
    response = client.post("/todos", json={"title": ""})
    assert response.status_code == 422


def test_create_todo_title_too_long(client):
    response = client.post("/todos", json={"title": "x" * 201})
    assert response.status_code == 422


def test_update_todo_null_title_rejected(client):
    create = client.post("/todos", json={"title": "Valid"})
    todo_id = create.json()["id"]
    response = client.patch(f"/todos/{todo_id}", json={"title": None})
    assert response.status_code == 422


def test_update_todo_null_completed_rejected(client):
    create = client.post("/todos", json={"title": "Valid"})
    todo_id = create.json()["id"]
    response = client.patch(f"/todos/{todo_id}", json={"completed": None})
    assert response.status_code == 422


def test_partial_update_preserves_other_fields(client):
    create = client.post("/todos", json={"title": "Original"})
    todo_id = create.json()["id"]
    client.patch(f"/todos/{todo_id}", json={"completed": True})
    response = client.get(f"/todos/{todo_id}")
    data = response.json()
    assert data["title"] == "Original"
    assert data["completed"] is True
