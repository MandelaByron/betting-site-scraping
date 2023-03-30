{
    "games":
    [
        {
            "season":"xxx", # type:str
            "start_time":"xxx", # type: timestamp
            "regions":{
                "Africa":{
                    "games":[
                        {
                            "btts":[
                                {
                                    "index":"xx", # type:int This is the position of the match
                                    "team_1":"xxx", # type:str
                                    "team_2":"xxx", # type:str
                                    "odds":{
                                        "Yes": "xxx", # type:float
                                        "No": "xxx" # type:float
                                    }
                                },
                                ...
                            ],
                            "o/u 2.5":[
                                {  
                                    "index":"xx", # type:int This is the position of the match
                                    "team_1":"xxx", # type:str
                                    "team_2":"xxx", # type:str
                                    "odds":{
                                        "Over": "xxx", # type:float
                                        "Under": "xxx" # type:float
                                    }
                                },
                                ...
                            ],
                            "1X2":[
                                {  
                                    "index":"xx", # type:int This is the position of the match
                                    "team_1":"xxx", # type:str
                                    "team_2":"xxx", # type:str
                                    "odds":{
                                        "1": "xxx", # type:float
                                        "x": "xxx", # type:float
                                        "2": "xxx", # type:float
                                    }
                                },
                                ...
                            ],
                            "dc":[
                                {  
                                    "index":"xx", # type:int This is the position of the match
                                    "team_1":"xxx", # type:str
                                    "team_2":"xxx", # type:str
                                    "odds":{
                                        "12": "xxx", # type:float
                                        "1x": "xxx", # type:float
                                        "2x": "xxx", # type:float
                                    }
                                },
                                ...
                            ],
    
                        }
                    ],
                    "Results":[
                        {
                            "team_1":"xxx", # type:str
                            "team_2":"xxx", # type:str
                            "team_1_score":"xxx", # type:int
                            "team_2_score":"xxx" # type:int
                        },
                        ...
                    ],
                    "League Table":[
                        {
                            "team":"xxx", # type:str
                            "W":"xxx", # type:str
                            "D":"xxx", # type:str
                            "L":"xxx", # type:str
                            "PTS":"xxx" # type:str
                        },
                        ...
                    ]
                    
                },
                "England":{...},
                "Spain":{...},
                "World":{...},
            }
        }
    ]
    
}
