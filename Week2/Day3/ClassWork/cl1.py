def process_data(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

process_data(1, 2, 3, name="Alice", age=30)
