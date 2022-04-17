from urllib import response
from flask import Flask, jsonify, make_response, render_template

app = Flask(__name__) 

@app.route("/test") 
def hello():
    # MAX_LEN = 11
    # url_set = UrlSettings(request, MAX_LEN)
    # handle_set = BojDefaultSettings(request, url_set)
    svg = '''
    <!DOCTYPE svg PUBLIC
        "-//W3C//DTD SVG 1.1//EN"
        "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<svg height="170" width="350"
    version="1.1"
    xmlns="http://www.w3.org/2000/svg"
    xmlns:xlink="http://www.w3.org/1999/xlink"
    xml:space="preserve">
    <style type="text/css">
        <![CDATA[
            @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;500;700&display=block');
            @keyframes delayFadeIn {{
                0%{{
                    opacity:0
                }}
                60%{{
                    opacity:0
                }}
                100%{{
                    opacity:1
                }}
            }}
            @keyframes fadeIn {{
                from {{
                    opacity: 0;
                }}
                to {{
                    opacity: 1;
                }}
            }}
            @keyframes rateBarAnimation {{
                0% {{
                    stroke-dashoffset: {bar_size};
                }}
                70% {{
                    stroke-dashoffset: {bar_size};
                }}
                100%{{
                    stroke-dashoffset: 35;
                }}
            }}
            .background {{
                fill: url(#grad);
            }}
            text {{
                fill: white;
                font-family: 'Noto Sans KR', sans-serif;
            }}
            text.boj-handle {{
                font-weight: 700;
                font-size: 1.45em;
                animation: fadeIn 0.8s ease-in-out forwards;
            }}
            text.tier-text {{
                font-weight: 700;
                font-size: 1.45em;
                opacity: 55%;
            }}
            text.tier-number {{
                font-size: 3.1em;
                font-weight: 700;
            }}
            .subtitle {{
                font-weight: 500;
                font-size: 0.9em;
            }}
            .value {{
                font-weight: 400;
                font-size: 0.9em;
            }}
            .percentage {{
                font-weight: 300;
                font-size: 0.8em;
            }}
            .progress {{
                font-size: 0.7em;
            }}
            .item {{
                opacity: 0;
                animation: delayFadeIn 1s ease-in-out forwards;
            }}
            .rate-bar {{
                stroke-dasharray: {bar_size};
                stroke-dashoffset: {bar_size};
                animation: rateBarAnimation 1.5s forwards ease-in-out;
            }}
        ]]>
    </style>
    <defs>
        <linearGradient id="grad" x1="0%" y1="0%" x2="100%" y2="35%">
            <stop offset="10%" style="stop-color:{color1};stop-opacity:1"></stop>
            <stop offset="55%" style="stop-color:{color2};stop-opacity:1"></stop>
            <stop offset="100%" style="stop-color:{color3};stop-opacity:1"></stop>
        </linearGradient>
    </defs>
    <rect width="350" height="170" rx="10" ry="10" class="background"/>
    <text x="315" y="50" class="tier-text" text-anchor="end" >{tier_title}{tier_rank}</text>
    <text x="35" y="50" class="boj-handle">{boj_handle}</text>
    <g class="item" style="animation-delay: 200ms">
        <text x="35" y="79" class="subtitle">rate</text><text x="145" y="79" class="rate value">{rate}</text>
    </g>
    <g class="item" style="animation-delay: 400ms">
        <text x="35" y="99" class="subtitle">solved</text><text x="145" y="99" class="solved value">{solved}</text>
    </g>
    <g class="item" style="animation-delay: 600ms">
        <text x="35" y="119" class="subtitle">class</text><text x="145" y="119" class="class value">{boj_class}{boj_class_decoration}</text>
    </g>
    <g class="rate-bar" style="animation-delay: 800ms">
        <line x1="35" y1="142" x2="{bar_size}" y2="142" stroke-width="4" stroke="floralwhite" stroke-linecap="round"/>
    </g>
    <line x1="35" y1="142" x2="290" y2="142" stroke-width="4" stroke-opacity="40%" stroke="floralwhite" stroke-linecap="round"/>
    <text x="297" y="142" alignment-baseline="middle" class="percentage">{percentage}%</text>
    <text x="293" y="157" class="progress" text-anchor="end">{now_rate} / {needed_rate}</text>
</svg>
    '''.format(color1='#FFC944',
               color2='#FFAF44',
               color3='#FF9632',
               boj_handle='이름',
               tier_rank='랭크',
               tier_title='티어이름',
               solved='솔브드',
               boj_class='클래스',
               boj_class_decoration='+',
               rate='레이트',
               now_rate='현재레이트',
               needed_rate='필경',
               percentage=80, # %
               bar_size=239) # 35 + 2.55 * 퍼센트

    response = make_response(svg)
    response.content_type = 'image/svg+xml'

    # return response
    return response

if __name__ == "__main__" :
    # app.run(host='127.0.0.1', port=8080, debug=True)
    app.run(host='0.0.0.0')

