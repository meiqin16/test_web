import pandas


class OperationExcel:
    def __init__(self, file_path):
        self.table = pandas.read_excel(file_path)

    def get_data_info(self):
        """获取表格详细信息"""
        data = []
        for v in self.table.index.values:
            data_dict = self.table.loc[v].to_dict()
            data.append(data_dict)
        return data

