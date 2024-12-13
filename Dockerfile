FROM python
# using python image from docker hub
WORKDIR /ashacode
# creating and changing folder in docker image
COPY automate2.py /Ashacode/
CMD [ "python" , "automate2.py" ]
# run the python code while creating container
