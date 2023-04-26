import requests
def Sample_program(Url):
    #the method to extract the dummy jason data
    try:
        response=requests.get(Url)
        print("printing the response of jason",response.status_code)
        print("printing the json fomat in text",response.text)
        print("printing the json in json format",response.json())
    except Exception:
        print("NOT POSSIBLE PERFORM THE OPERATIONS")

Sample_program("https://www.python.org")