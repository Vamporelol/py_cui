import py_cui
  
root = py_cui.PyCUI(10, 10)
root.add_button("Quit", 0, 0, command=exit)
root.add_label("info", 5, 0)
cb = root.add_checkbox_menu("Box", 3, 5)
cb.add_item("test1")
cb.add_item("test2")
root.add_label("info2", 8, 0)
root.add_label("info2", 5, 5)
root.add_label("info2", 0, 8)
root.add_label("info2", 0, 5)
root.start()