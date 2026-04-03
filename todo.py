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
            "completed" : False,
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
    def category_data(self):
        data = self.get_data()
        if not data:
            return
        category = self.state["category"]
        if category != "all":
            category_data = [dic for dic in data if dic["category"] ==category]
        else:
            category_data = data
        return category_data
    def set_category(self,category):
        self.state["category"] = category
        return
    def sorted_data(self):
        data = self.get_data()
        sort_column = self.state["sort_column"]
        sort_direction = self.state["sort_direction"]
        if not data:
            return
        
    def set_sort(self,column):
        pass
    def keyword_data(self):
        pass
    def set_keyword(self,keyword):
        pass
    def delete_data(self,idx):
        pass
    def set_completed(self,idx):
        pass
    def update_data(self,idx):
        pass
    def view_data(self):
        pass

