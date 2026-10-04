from flask import Flask, render_template_string, request,jsonify

app = Flask(__name__)

PASSWORD = "1234"

MESSAGE = """
May you always be surrounded by happiness, love, and good memories.I hope all your dreams come true and every new day brings you a reason to smile. Always take care and stay happy!🌷💗

Thank you for being a special person in my life.
I hope we can make many beautiful memories together.🥺💕

Always stay happy! 🌷
"""

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Our Special Gift 💗</title>

    <style>
        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            min-height: 100vh;
            background: #f5b7ce;
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            color: #a33d67;
        }

        .phone {
            width: 360px;
            max-width: 92%;
            min-height: 620px;
            background: #f6bfd5;
            padding: 25px 18px;
            border-radius: 28px;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .card {
            width: 100%;
            background: #fffafd;
            border-radius: 25px;
            padding: 28px 22px;
            text-align: center;
            box-shadow: 0 8px 25px #c98ba5;
        }

        .icon {
            font-size: 35px;
        }

        h1 {
            font-size: 21px;
            margin: 10px 0 5px;
        }

        .sub {
            font-size: 11px;
            color: #b77a95;
            margin-bottom: 20px;
        }

        #display {
            height: 42px;
            border: 1px solid #e6adc5;
            border-radius: 25px;
            display: flex;
            align-items: center;
            justify-content: center;
            letter-spacing: 7px;
            margin-bottom: 20px;
            background: white;
        }

        .keypad {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 12px;
        }

        button {
            border: none;
            cursor: pointer;
        }

        .key {
            height: 48px;
            border-radius: 50%;
            background: white;
            color: #a33d67;
            font-size: 16px;
            box-shadow: 0 4px 10px #e5bfd0;
        }

        .key:active {
            transform: scale(.9);
        }

        #home,
        #message,
        #music,
        #gallery {
            display: none;
        }

        .menu {
            display: flex;
            flex-direction: column;
            gap: 13px;
        }

        .item {
            background: white;
            border-radius: 16px;
            padding: 16px;
            display: flex;
            align-items: center;
            text-align: left;
            box-shadow: 0 4px 12px #ead2dc;
            cursor: pointer;
        }

        .item-icon {
            font-size: 27px;
            width: 48px;
        }

        .item strong {
            font-size: 14px;
        }

        .item small {
            display: block;
            color: #b8899e;
            margin-top: 4px;
        }

        .arrow {
            margin-left: auto;
            font-size: 22px;
        }

        .message {
            background: white;
            padding: 18px;
            border-radius: 16px;
            text-align: left;
            white-space: pre-line;
            line-height: 1.7;
            font-size: 13px;
        }

        .back {
            margin-top: 20px;
            background: #f3bfd4;
            color: #9d3f67;
            padding: 10px 22px;
            border-radius: 20px;
        }

        .music {
            background: white;
            border-radius: 18px;
            padding: 25px 15px;
        }

        .music-icon {
            font-size: 55px;
        }

        .photos {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 12px;
        }
photo {
            height: 130px;
            border-radius: 16px;
            background: #f8c8da;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 40px;
        }
    </style>
</head>

<body>

<div class="phone">

    <!-- PASSWORD -->
    <div class="card" id="lock">

        <div class="icon">💗 🔒</div>

        <h1>Unlock your special gift</h1>

        <div class="sub">
            Enter 4 digit code 💌
        </div>

        <div id="display"></div>

        <div class="keypad">

            <button class="key" onclick="press(1)">1</button>
            <button class="key" onclick="press(2)">2</button>
            <button class="key" onclick="press(3)">3</button>

            <button class="key" onclick="press(4)">4</button>
            <button class="key" onclick="press(5)">5</button>
            <button class="key" onclick="press(6)">6</button>

            <button class="key" onclick="press(7)">7</button>
            <button class="key" onclick="press(8)">8</button>
            <button class="key" onclick="press(9)">9</button>

            <button class="key" onclick="backspace()">⌫</button>
            <button class="key" onclick="press(0)">0</button>
            <button class="key" onclick="clearCode()">↺</button>

        </div>
    </div>


    <!-- HOME -->
    <div class="card" id="home">

        <h1>For my Fav Someone Special!💗</h1>

        <div class="sub">
            Just enjoy the memories 🥺🌷
        </div>

        <div class="menu">

            <div class="item" onclick="openPage('message')">
                <div class="item-icon">💌</div>
                <div>
                    <strong>Message</strong>
                    <small>Love Letter</small>
                </div>
                <div class="arrow">›</div>
            </div>

            <div class="item" onclick="openPage('music')">
                <div class="item-icon">🎵</div>
                <div>
                    <strong>Favorite Music</strong>
                    <small>Our Melody</small>
                </div>
                <div class="arrow">›</div>
            </div>

            <div class="item" onclick="openPage('gallery')">
                <div class="item-icon">📷</div>
                <div>
                    <strong>Gallery</strong>
                    <small>Precious Memories</small>
                </div>
                <div class="arrow">›</div>
            </div>

        </div>
    </div>


    <!-- MESSAGE -->
    <div class="card" id="message">

        <h1>💌 Message</h1>

        <div class="message">
            {{ message }}
        </div>

        <button class="back" onclick="goHome()">
            ← Back
        </button>

    </div>


    <!-- MUSIC -->
    <div class="card" id="music">

        <h1>🎵 Favorite Music</h1>

        <div class="music">

            <div class="music-icon">🎶</div>

            <p>Our Special Song 💗</p>

            <p>
                Perfect , Mann Mera ,Jatuh Suka ,Senorita , To the Bone
            </p>

        </div>

        <button class="back" onclick="goHome()">
            ← Back
        </button>

    </div>


    <!-- GALLERY -->
    <div class="card" id="gallery">

        <h1>📷 Gallery</h1>

        <div class="photos">

            <div class="photo">💗</div>
            <div class="photo">🌷</div>
            <div class="photo">🥺</div>
            <div class="photo">🫶</div>

        </div>

        <button class="back" onclick="goHome()">
            ← Back
        </button>

    </div>

</div>


<script>

let code = "";

function press(number) {

    if (code.length < 4) {

        code += number;

        document.getElementById("display").innerText =
            "●".repeat(code.length);
    }

    if (code.length === 4) {
        checkPassword();
    }
}


function checkPassword() {

    fetch("/check", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            password: code
        })

    })
    .then(response => response.json())

    .then(data => {

        if (data.correct) {

            document.getElementById("lock").style.display = "none";

            document.getElementById("home").style.display = "block";

        } else {

            alert("Wrong password 💗");

            clearCode();
        }

    });
}


function clearCode() {

    code = "";

    document.getElementById("display").innerText = "";
}


function backspace() {

    code = code.slice(0, -1);

    document.getElementById("display").innerText =
        "●".repeat(code.length);
}


function openPage(page) {

    document.getElementById("home").style.display = "none";

    document.getElementById("message").style.display = "none";
    document.getElementById("music").style.display = "none";
    document.getElementById("gallery").style.display = "none";

    document.getElementById(page).style.display = "block";
}


function goHome() {

    document.getElementById("message").style.display = "none";
    document.getElementById("music").style.display = "none";
    document.getElementById("gallery").style.display = "none";

    document.getElementById("home").style.display = "block";
}

</script>

</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(
        HTML,
        message=MESSAGE
    )


@app.route("/check", methods=["POST"])
def check():

    data = request.get_json()

    correct = data["password"] == PASSWORD

    return jsonify({
        "correct": correct
    })


if __name__ == "__main__":
    app.run(debug=True)