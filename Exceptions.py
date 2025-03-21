try:
    print(5/0)

# except ZeroDivisionError as e:
#     print(type(e).__name__ + "Error Occurred!")

except Exception as e:
    print(type(e).__name__ + "Error Occurred")