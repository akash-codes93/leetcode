var request = require('request');


let set_evaluation = (data, token, account) => {
    data = JSON.parse(data);

    console.log(data);


    if (data["data"].length == 0) {
        console.log("Nothing to evaluate: " + account)
        return null;
    }

    let uuid = data["data"][0]["rounds"][0]["uuid"]
    console.log(uuid);

    let set_evaluator = {
        'method': 'POST',
        'url': `https://api.relevel.com/api/v2/exams/evaluation/${uuid}/set-evaluator/`,
        'headers': {
            'authority': 'api.relevel.com',
            'accept': 'application/json',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'authorization': `Bearer ${token}`,
            'content-type': 'application/json',
            'origin': 'https://relevel.com',
            'platform': 'desktop_web',
            'referer': 'https://relevel.com/',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
            'x-origin-panamera': 'ocla-85_olx.com.tr'
        },
        body: JSON.stringify({})
    };

    request(set_evaluator, function (error, response) {
        if (error) throw new Error(error);
        console.log(response.body + " " + account);
        console.log("An interview assigned: " + account)
        process.exit(1);
    });

}

let get_evaluation = (token, account) => {

    let check_evaluations = {
        'method': 'GET',
        'url': 'https://api.relevel.com/api/v2/exams/evaluation/rounds/?is_pending=True',
        'headers': {
            'authority': 'api.relevel.com',
            'accept': 'application/json',
            'accept-language': 'en-GB,en;q=0.9',
            'authorization': `Bearer ${token}`,
            'origin': 'https://relevel.com',
            'platform': 'desktop_web',
            'referer': 'https://relevel.com/',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
        }
    };

    request(check_evaluations, function (error, response) {
        if (error) throw new Error(error);
        // console.log(response.body + " " + account);
        set_evaluation(response.body, token, account)
    });

}


let start = async () => {

    while (true) {
        get_evaluation('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjYwNTY1OTg2LCJqdGkiOiI1OGU5ODI4MzY4MTg0MjM0YTZkYjUwNmI5YjlkMmZiZCIsInVzZXJfaWQiOjEyODYyN30.2AILz7YJDiB1zzEnr107kdjI_ND7AMkrGrRoVeI-OTo', "Normal")
        get_evaluation('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjYxMjUxMTY4LCJqdGkiOiJlNjNkMWNiMmFmOGE0ODk3OWRkNjljNjZmNjFkNDRhZiIsInVzZXJfaWQiOjE4MzIzNDR9.VD-G0h4UUNtXH4BBd7ywlPPQEVC9Rby2UqjRMTN5pW8', "Courses")
        const delay = ms => new Promise(resolve => setTimeout(resolve, ms))
        await delay(10000)
    }

}

start()


