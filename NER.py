import google.generativeai as genai

genai.configure(api_key="ENTER_YOUR_API")
model = genai.GenerativeModel("gemini-1.5-flash")

# Read the entire content of output.txt
with open('output.txt', 'r', encoding='utf-8') as file:
    content = file.read()

testNER = "Do Named Entity Relationship for below in JSON in detail where equipment is main object: " + content
# print(testNER)

NER = testNER

response = model.generate_content(NER)
print(response.text)
