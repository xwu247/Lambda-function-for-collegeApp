'use strict';

console.log('Loading function');

const aws = require('aws-sdk');

const s3 = new aws.S3({ apiVersion: '2006-03-01' });
var message;
var ToneAnalyzerV3 = require('https://gateway.watsonplatform.net/tone-analyzer/api');

exports.handler = (event, context, callback) => {
    //console.log('Received event:', JSON.stringify(event, null, 2));

    // Get the object from the event and show its content type
    const bucket = event.Records[0].s3.bucket.name;
    const key = decodeURIComponent(event.Records[0].s3.object.key.replace(/\+/g, ' '));
    const params = {
        Bucket: bucket,
        Key: key,
    };
    s3.getObject(params, (err, data) => {
        if (err) {
            console.log(err);
            message = `Error getting object ${key} from bucket ${bucket}.`;
            console.log(message);
            callback(message);
        } else {
            console.log('CONTENT TYPE:', data.ContentType);
            callback(null, data.ContentType);
        }
    });

        
    var tone_analyzer = new ToneAnalyzerV3({
      username: '25aff8c5-4afd-4b18-aed8-12bab8d78090',
      password: '5dAUlipzhPdj',
      version_date: '2016-02-11'
    });
    
    var params2 = {
      // Get the text from the JSON file.
      text: "curry is funny",
      tones: 'emotion'
    };
    
    tone_analyzer.tone(params2, function(error, response) {
      if (error)
        console.log('error:', error);
      else
        console.log(JSON.stringify(response, null, 2));
      }
    );
};
