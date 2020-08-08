# aDjangoApi


•    Django Api for Insert, Select and Update.

     1.   API DETAILS :- ,
          {
            "info": "api information",
            "for insertdata": [
                {
                    "api call": "https://adjangoapi.herokuapp.com/insertion",
                    "input key": [
                        "id",
                        "real_name",
                        "tz",
                        "activity_periods"
                    ]
                }
            ],
            "for selection": [
                {
                    "api call": "https://adjangoapi.herokuapp.com/selection",
                    "input key": "id"
                }
            ],
            "path": [
                "TestJSON.json"
            ]
        }
        
     2.   At the time of insert data if you are passing duplicate id then it will update your data,
     
•    Output :-
      
      1.  For Insert - 
          {
            "Status": "Sucess",
            "Api Name": "/insertion"
          }
          
      2.  For Update - 
          {
            "Status": "Updation Sucess",
            "Reason": "ID is already existing",
            "Api Name": "/insertion"
         }
         
      3.  For Select - 
          {
              "id": "sudhir002",
              "real_name": " sudhir kumar",
              "tz": "abs",
              "activity_periods": [
                  {
                      "start_time": "xyz",
                      "end_time": "qwe"
                  }
              ]
          }
          
         
