from ..model.init_tableindex import TableIndex


class PSIndex:
    def __init__(self, index: TableIndex) -> None:
        self.index = index

    def getIndex(self):
        return self.index

    def getKey(self):
        if self.index.isPrimaryKey():
            return " class='primaryKey' title='Primary Key'"
        elif self.index.isUniqueKey():
            return " class='uniqueKey' title='Unique Key'"
        else:
            return " title='Indexed'"

    def getKeyIcon(self):
        return (
            "<i class='icon ion-key iconkey'></i> "
            if self.index.isPrimaryKey() or self.index.isUniqueKey()
            else ""
        )
