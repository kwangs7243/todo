import datetime as dt
class todo:
    def __init__(self):
        self.state = {
            "sort_column" : None,
            "sort_direction" : None,
            "category" : "active",
            "keyword" : None
        }
        self.todos = []
    def add_todo(self,content):
        date = dt.datetime.now().strftime("%y-%m-%d")
        content = content.strip()
        info= {
            "date" : date,
            "content" : content,
            "category" : "active",
            "deleted" : False,
        }
        self.todos.append(info)
        return
    def get_data(self):
        if not self.todos:
            return
        data=[]
        for idx,dic in enumerate(self.todos):
            new_dic = dic.copy()
            new_dic["original_idx"] = idx
            data.append(new_dic)
        return data
    def set_category(self,category):
        self.state["category"] = category
        return
    def set_sort(self,column):
        if column != self.state["sort_column"]:
            self.state["sort_column"] = column
            self.state["sort_direction"] = "asc"
            return
        if self.state["sort_direction"] == "asc":
            self.state["sort_direction"] = "desc"
            return
    def set_keyword(self,keyword):
        keyword = keyword.strip()
        self.state["keyword"] = keyword
        return
    def category_data(self):
        category_data = self.get_data()
        if not category_data:
            return  
        category = self.state["category"]
        if category != "all":
            category_data = [dic for dic in category_data if dic["category"] == category]
        return category_data
    def sorted_data(self):
        sorted_data = self.get_data()
        if not sorted_data:
            return
        column = self.state["sort_column"]
        direction = self.state["sort_direction"]
        if column is not None:
            if direction == "asc":
                sorted_data = sorted(sorted_data,key=lambda x:x[column],reverse=False)
            else:
                sorted_data = sorted(sorted_data,key=lambda x:x[column],reverse=True)
        return sorted_data
    def keyword_data(self):
        keyword_data = self.get_data()
        if not keyword_data:
            return
        keyword = self.state["keyword"]
        keyword_data = [dic for dic in keyword_data if keyword in dic["content"]]
        return keyword_data
    def delete_data(self,number):
        try:
            original_idx = int(number) - 1
        except:
            return
        self.todos[original_idx]["deleted"] == True
        return
    def set_completed(self,number):
        try:
            original_idx = int(number) - 1
        except:
            return
        self.todos[original_idx]["completed"] = True
        return
    def update_data(self,number,content):
        content = content.strip()
        if not content:
            return
        try:
            original_idx = int(number) - 1
        except:
            return
        self.todos[original_idx]["content"] = content
        return
    def view_data(self):
        view_data = self.get_data()
        view_data = self.keyword_data(view_data)
        if not view_data:
            return
        view_data = self.category_data(view_data)
        view_data = self.sorted_data(view_data)
        return view_data

