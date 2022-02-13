FROM python:3
ADD getUser.py /
CMD [ "python3", "./getUser.py" ]
# OR CMD ["python","/app/my_py.py"]