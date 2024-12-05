 def search_record(self):
        website = self.search_entry.get()
        records = self.db.search_records(website)
        for item in self.records_tree.get_children():
            self.records_tree.delete(item)
        for record in records:
            self.records_tree.insert('', 'end', values=record)
