html_header = """
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>F1 Bingo Card Generator</title>
            <script>
            var count=1;
            function setColor(btn, color){
                var property = document.getElementById(btn);
                if (count == 0){
                    property.style.backgroundColor = "#000000"
                    count=1;        
                }
                else{
                    property.style.backgroundColor = "#7FFF00"
                    count=0;
                }

            }
            </script>
        </head>
        <style>

            body {
              margin: 40px;
            }

            .box {
              background-color: black;
              color: #fff;
              border-radius: 5px;
              padding: 10px;
              font-size: 85%;
              text-align: center;
            }

            .header {
                background-color: black;
                color: #fff;
                border-radius: 5px;
                padding: 10px;
                text-align: center;
                width: 520px;
                margin-bottom: 10px;
            }

            .wrapper {
              width: 600px;
              display: grid;
              grid-gap: 10px;
              grid-template-columns: repeat(5, 100px);
              grid-template-rows: repeat(5, 100px);
              grid-auto-flow: column;

            }
        </style>

        <div class="header" id="headr" onclick="setColor('headr', '#101010')">VROOMATES F1 BINGO</div>

        """

html_tail = """
        </body>
        </html>
"""
teams = [
        "Mercedes", "Ferrari", "Red Bull", "Alpha Tauri",
        "Haas", "Aston Martin", "Alfa Romeo", "Williams",
        "McLaren", "Alpine"
    ]

generic = [
        "{} investigated by race control",
        "Shot of {} pit", 
    ]

unique = [
        "Lewis micromanages", 
        "Yuki swears", 
        "Ferrari infighting", 
        "5 second penalty", 
        "Pit stop under 2 seconds", 
        "Pit stop over 4 seconds", 
        "Speculation about second Mercedes seat 2022", 
        "“Debris”", 
        "Fun fact about host country", 
        "Wing damage", 
        "Tire damage", 
        "Yellow flag", 
        "Max unintelligible on the radio", 
        "“Marbles”", 
        "Mention someone’s dad", 
        "Show someone’s dad", 
        "“Box box box”", 
        "Show a POC not related to a driver", 
        "Driver told to switch plans",
        "3+ DNFs", 
        "Christian Horner jiggling foot", 
        "Blue flag penalty", 
        "Toto Wolff extreme closeup", 
        "“Chicane”",
        "Safety car!!!",
        "Mention Kimi's age or longevity",
        "Anyone invokes Senna",
        "Discussion of a driver doing an extremely rich person activity",
        "“Downforce”",
        "Driver comments on wind",
        "DRS overtake",
        "Spinout"
        ]