import json

student_details="""{
	"first_name": "puneet",
	"last_name": "bansal",
	"age": 21,
	"sex": "male",
	"contact_details": {
		"mobile": [8964526276, 9426738263],
		"landline": "014562671892",
		"email": "puneetbansal77@ymail.com"
	},
	"course": "b.tech(cse)",
	"education_details": {
		"12th": "2016",
		"10th": "2014",
		"ug": "2020"
	},
	"languages": ["c", "c++", "java", "python"],
	"scholarship": True

}"""
    
with open("studnet1.json","w") as file:
    json.dump(student_details,file)