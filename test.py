import todo as td
def test_add_todo():
    t = td.todo()
    t.add_todo("test1")
    t.add_todo("test2")
    data = t.get_data()
    print(len(data) == 2)
    print(data[0]["content"] == "test1")
    print(data[1]["content"] == "test2")
def test_category():
    t = td.todo()
    t.add_todo("test1")
    t.add_todo("test2")
    t.set_category("active")
    category_data = t.category_data()
    print(len(category_data) == 2)
    print(category_data[0]["content"] == "test1")
    print(category_data[1]["content"] == "test2")
    print(category_data[0]["category"] == "active")
    print(category_data[1]["category"] == "active") 

test_add_todo()
test_category()