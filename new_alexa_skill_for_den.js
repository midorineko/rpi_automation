'use strict';
exports.handler = function (event, context) {
var http = require( 'http' );
var https = require( 'https' );
var url = 'https://56cd5017.ngrok.io/';

    try {
        console.log("event.session.application.applicationId=" + event.session.application.applicationId);

        if (event.session.new) {
            onSessionStarted({requestId: event.request.requestId}, event.session);
        }

        if (event.request.type === "LaunchRequest") {
            onLaunch(event.request,
                event.session,
                function callback(sessionAttributes, speechletResponse) {
                    context.succeed(buildResponse(sessionAttributes, speechletResponse));
                });
        } else if (event.request.type === "IntentRequest") {
            onIntent(event.request,
                event.session,
                function callback(sessionAttributes, speechletResponse) {
                    context.succeed(buildResponse(sessionAttributes, speechletResponse));
                }, event);
        } else if (event.request.type === "SessionEndedRequest") {
            onSessionEnded(event.request, event.session);
            context.succeed();
        }
    } catch (e) {
        context.fail("Exception: " + e);
    }
};

/**
 * Called when the session starts.
 */
function onSessionStarted(sessionStartedRequest, session) {
    console.log("onSessionStarted requestId=" + sessionStartedRequest.requestId
        + ", sessionId=" + session.sessionId);
}

function onLaunch(launchRequest, session, callback) {
    console.log("onLaunch requestId=" + launchRequest.requestId
        + ", sessionId=" + session.sessionId);

    var cardTitle = "Hello, World!"
    var speechOutput = "You can tell Hello, World! to say Hello, World!"
    callback(session.attributes,
        buildSpeechletResponse(cardTitle, speechOutput, "", true));
}

function onIntent(intentRequest, session, callback, eventPassed) {
    console.log("onIntent requestId=" + intentRequest.requestId
        + ", sessionId=" + session.sessionId);

    var intent = intentRequest.intent,
        intentName = intentRequest.intent.name;

    var current = '';
    var den_type = '';
    if (intentName == 'DenIntent') {
        if(eventPassed.request.intent.slots.textile.value){
            current = eventPassed.request.intent.slots.textile.value.toLowerCase();
            den_type = 'scene';
        }else if(eventPassed.request.intent.slots.brightness.value){
            current = eventPassed.request.intent.slots.brightness.value;
            den_type = 'brightness';
        }
        handleDenRequest(intent, session, callback, current, den_type);
    }
    else {
        throw "Invalid intent";
    }
}
function onSessionEnded(sessionEndedRequest, session) {
    console.log("onSessionEnded requestId=" + sessionEndedRequest.requestId
        + ", sessionId=" + session.sessionId);
}

function handleDenRequest(intent, session, callback, current, den_type) {
    var https = require( 'https' );
    var send_url = 'https://d6135033.ngrok.io/'
    var send_text = '';
    if(den_type == 'scene'){
        var no_spaces = current.replace(/\s+/g, '');
        send_url = send_url + 'scene_select/' + no_spaces;
        send_text = 'Den set to ' + current;
    }else if(den_type == 'brightness'){
        send_url = send_url + 'brightness/' + current;
        send_text = 'Brightness set to ' + current;
    }
    https.get( send_url, function( ) {} );
                callback(session.attributes,
        buildSpeechletResponseWithoutCard(send_text, "", "true"));
}
function buildSpeechletResponse(title, output, repromptText, shouldEndSession) {
    return {
        outputSpeech: {
            type: "PlainText",
            text: output
        },
        card: {
            type: "Simple",
            title: title,
            content: output
        },
        reprompt: {
            outputSpeech: {
                type: "PlainText",
                text: repromptText
            }
        },
        shouldEndSession: shouldEndSession
    };
}

function buildSpeechletResponseWithoutCard(output, repromptText, shouldEndSession) {
    return {
        outputSpeech: {
            type: "PlainText",
            text: output
        },
        reprompt: {
            outputSpeech: {
                type: "PlainText",
                text: repromptText
            }
        },
        shouldEndSession: shouldEndSession
    };
}

function buildResponse(sessionAttributes, speechletResponse) {
    return {
        version: "1.0",
        sessionAttributes: sessionAttributes,
        response: speechletResponse
    };
}