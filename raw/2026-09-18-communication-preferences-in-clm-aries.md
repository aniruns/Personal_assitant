---
title: "Communication Preferences in CLM - Aries"
source: "https://zeta-tm.atlassian.net/wiki/spaces/ARIES/pages/3558114469/Communication+Preferences+in+CLM"
author:
published:
created: 2026-09-18
description:
tags:
  - "clippings"
redaction: "2026-09-18: the sample X-Zeta-AuthToken JWT in the curl example was replaced with <REDACTED-JWT> before commit (pre-commit Gitleaks hook). No other content changed."
---
## Communication Preferences in CLM

## Types of messages supported today

Currently, Notifications Centre supports eight types of messages -

- Critical - Critical messages refer to important, urgent, or sensitive communications that must be handled with priority to ensure smooth operations, compliance, and risk management including fraud alerts, system outages, regulatory notifications, security breaches, transaction failures, customer legal matters, credit risk and delinquency messages.
- Directed - These messages refer to communications that are specifically targeted or sent to a particular individual to ensure timely and appropriate action. These messages could include customer alerts, action requests or regulatory or compliance messages for the individual such as KYC action.
- OTP - These messages usually are used to send OTP messages to customers
- Authentication - These messages are used when a customer needs to be approved or authorized.
- Promotional - These messages referto communications that are sent to customers or potential customers with the purpose of promoting products, services, or special offers. These messages are typically aimed at increasing customer engagement, encouraging the use of certain bank services, or driving sales of financial products.
- Announcement - Announcement messages in a bank refer to communications that inform customers about important updates, changes, events, or new developments related to the bank's operations, policies, or services.
- Transactional - Transactional messages refer to communications that are triggered by specific actions or transactions made by a customer.
- Default - Default messages refer to standardized or pre-set communications that are automatically generated or used when certain conditions or events occur. These messages are typically generic and may not be tailored to specific customers or situations, but they provide basic information or instructions.

## Types of Channels Supported Today

<table><colgroup><col> <col> <col> <col></colgroup><tbody><tr><th rowspan="1" colspan="1"><div><p><strong>Channel</strong></p><figure></figure></div></th><th rowspan="1" colspan="1"><div><p><strong>Provider</strong></p><figure></figure></div></th><th rowspan="1" colspan="1"><div><p><strong>Used For</strong></p><figure></figure></div></th><th rowspan="1" colspan="1"><div><p><strong>Used In</strong></p><figure></figure></div></th></tr></tbody></table>

<table><colgroup><col> <col> <col> <col></colgroup><tbody><tr><th rowspan="1" colspan="1"><div><p><strong>Channel</strong></p><figure></figure></div></th><th rowspan="1" colspan="1"><div><p><strong>Provider</strong></p><figure></figure></div></th><th rowspan="1" colspan="1"><div><p><strong>Used For</strong></p><figure></figure></div></th><th rowspan="1" colspan="1"><div><p><strong>Used In</strong></p><figure></figure></div></th></tr><tr><td rowspan="1" colspan="1"><p>SMS</p></td><td rowspan="1" colspan="1"><p>Sinch(ACL), GupShup, Twilio, TLRX ( Common Prod )</p></td><td rowspan="1" colspan="1"></td><td rowspan="1" colspan="1"><p>HDFC, Pixel</p></td></tr><tr><td rowspan="1" colspan="1"><p>Email</p></td><td rowspan="1" colspan="1"><p>Karix, Sengrid</p></td><td rowspan="1" colspan="1"></td><td rowspan="1" colspan="1"></td></tr><tr><td rowspan="1" colspan="1"><p>Flow</p></td><td rowspan="1" colspan="1"><p>Twilio, Plivo</p></td><td rowspan="1" colspan="1"><p>Sending IVR calls</p></td><td rowspan="1" colspan="1"></td></tr><tr><td rowspan="1" colspan="1"><p>Inbox</p></td><td rowspan="1" colspan="1"><p>Collection</p></td><td rowspan="1" colspan="1"><p>Notification inside the App ( In app )</p></td><td rowspan="1" colspan="1"><p>Specifically for Cardworks</p></td></tr><tr><td rowspan="1" colspan="1"><p>Printed Letters</p></td><td rowspan="1" colspan="1"><p>IO to put files in SFTP</p></td><td rowspan="1" colspan="1"><p>Place PDF file in SFTP owned by Sparrow or Cardworks</p></td><td rowspan="1" colspan="1"><p>Only US</p></td></tr><tr><td rowspan="1" colspan="1"><p>Push</p></td><td rowspan="1" colspan="1"><p>Andriod ( Firebase Cloud Messaging )</p><p>IOS ( Apple push notification service )</p></td><td rowspan="1" colspan="1"></td><td rowspan="1" colspan="1"></td></tr><tr><td rowspan="1" colspan="1"><p>Spotlight</p></td><td rowspan="1" colspan="1"><p>Collection</p></td><td rowspan="1" colspan="1"><p>Popup notification inside Pluxee app.</p></td><td rowspan="1" colspan="1"><p>Only used by Pluxee</p></td></tr></tbody></table>

## How CLM supports these messages at AH level

Currently, CLM enables consent of each of these messages by the use of **communication preferences -**

The communication preferences at AH level would look like this -

```
"pointsOfPresence": [

      {

          "id": "f542b54e-c692-47e7-8374-e8fedc084ba7",

          "ifiID": 600309,

          "accountHolderId": "29b55cec-5885-49d4-b76c-df590a3d0081",

          "label": "Billing",

          "addresses": [

              {

                  "id": "80c679a0-b3a5-4b02-b5fb-25e748197918",

                  "type": "Postal",

                  "value": {

                      "city": "Bangalore",

                      "line1": "7C, 1st A Main Rd, MCHS Colony",

                      "line2": "Sector 6",

                      "line3": "HSR Layout",

                      "state": "Karnataka",

                      "country": "US",

                      "postCode": "56010"

                  },

                  "isCommunicationAllowed": true,

                  "tags": [

                      {

                          "type": "COMMUNICATION_PREFERENCE",

                          "value": "DEFAULT",

                          "attributes": {

                              "disallowedChannels": "SMS,CALL"

                          }

                      }

                  ],

                  "attributes": {

                      "nearestLandmark": "State Bank of India",

                      "communicationPreferences": "true"

                  },

                  "headers": {}

              }

          ],

      },

      {

          "id": "4f32b037-0bb7-4c4c-9fb5-5ced9f76220e",

          "ifiID": 600309,

          "accountHolderId": "29b55cec-5885-49d4-b76c-df590a3d0081",

          "label": "Communication",

          "addresses": [

              {

                  "id": "4382ab90-1f54-43b5-ad9e-b7c80cf72f40",

                  "type": "Email",

                  "value": "+Ruth_Lebsack20@yahoo.com",

                  "isCommunicationAllowed": true,

                  "tags": [

                      {

                          "type": "COMMUNICATION_PREFERENCE",

                          "value": "ANNOUNCEMENT",

                          "attributes": {

                              "disallowedChannels": ""

                          }

                      },

                      {

                          "type": "COMMUNICATION_PREFERENCE",

                          "value": "CRITICAL",

                          "attributes": {

                              "disallowedChannels": ""

                          }

                      },

                      {

                          "type": "COMMUNICATION_PREFERENCE",

                          "value": "DEFAULT",

                          "attributes": {

                              "disallowedChannels": "SMS,CALL"

                          }

                      },

                      {

                          "type": "COMMUNICATION_PREFERENCE",

                          "value": "DIRECTED",

                          "attributes": {

                              "disallowedChannels": ""

                          }

                      }

                  ],

                  "attributes": {

                      "communicationPreferences": "true"

                  },

                  "headers": {}

              }

          ],

          "isDefault": false,

          "attributes": {

              "nearestLandmark": "State Bank of India"

          },

         

      },

      {

          "id": "b4504edb-bb34-4c07-b4a4-4917d6c142ef",

          "ifiID": 600309,

          "accountHolderId": "29b55cec-5885-49d4-b76c-df590a3d0081",

          "label": "Home",

          "addresses": [

              {

                  "id": "b5eb614a-5c5a-4d92-976a-24eff2dd7a5a",

                  "type": "Phone",

                  "value": "+12783928391",

                  "isCommunicationAllowed": true,

                  "tags": [

                      {

                          "type": "COMMUNICATION_PREFERENCE",

                          "value": "CRITICAL",

                          "attributes": {

                              "disallowedChannels": ""

                          }

                      },

                      {

                          "type": "COMMUNICATION_PREFERENCE",

                          "value": "DEFAULT",

                          "attributes": {

                              "disallowedChannels": "SMS,CALL"

                          }

                      },

                      {

                          "type": "COMMUNICATION_PREFERENCE",

                          "value": "DIRECTED",

                          "attributes": {

                              "disallowedChannels": ""

                          }

                      }

                  ],

                  "attributes": {

                      "communicationPreferences": "true"

                  },

                  "headers": {}

              }

          ],

          "isDefault": false,

          "createdAt": "2024-05-30T15:26:16.530+05:30",

          "updatedAt": "2025-01-02T14:40:40.401+05:30",

          "createdBy": "i6t1bu6oGb0kyToL0XnPwA==@authProfile.600309-admin.India/9901",

          "updatedBy": "i6t1bu6oGb0kyToL0XnPwA==@authProfile.600309-admin.India/9901"

      },

          ]
```

As seen from the aforementioned response structure, communication preferences are defined at each POP level. Therefore, CLM gives the flexibility to the issuer to define and set their communication preferences at a particular email or phone level.

## Consent Capture

CLM stores communication preferences under tags at POP address level. Details stored as part of communication preferences -

- Type of communication Preference - CRITICAL, AUTHENTICATION, OTP, DEFAULT, TRANSACTIONAL, PROMOTIONAL, ANNOUNCEMENT, DIRECTED
- Disallowed channels - These are the channels through which the customer prefers not to receive a specific type of message.

There is a parent consent at POP level called `"isCommunicationAllowed"`.

- if `isCommunicationAllowed` is false then **except OTP** no other messages will be allowed on that address (postal, phone, email)
- if `isCommunicationAllowed` is true then individual communication preferences can be added and they can either be allowed by keeping disallowed channels as an empty string **(**` "disallowedChannels": ""`**)** or can be disallowed by mentioning the disallowed channels (`"disallowedChannels": "SMS,CALL"`)
- Notifications centre updates communication preferences based on the event published by CLM. Communication preferences for an Account Holder published by CLM overrides any existing communication preferences present at Notifications centre for Account Holder.

## Update Communication Preferences

Communication preferences can be updated at CLM by using the curl -

```
curl --location 'https://aries.internal.mum1-pp.zetaapps.in/mars/tachyon/v4/ifi/600309/accountholders/29b55cec-5885-49d4-b76c-df590a3d0081/communicationPreferences/update' \

--header 'Accept: application/json, text/plain, */*' \

--header 'Accept-Language: en-GB,en-US;q=0.9,en;q=0.8' \

--header 'Connection: keep-alive' \

--header 'Content-Type: application/json' \

--header 'Origin: http://localhost:8081' \

--header 'Referer: http://localhost:8081/' \

--header 'Sec-Fetch-Dest: empty' \

--header 'Sec-Fetch-Mode: cors' \

--header 'Sec-Fetch-Site: cross-site' \

--header 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36' \

--header 'X-Zeta-AuthToken: <REDACTED-JWT>' \

--header 'sec-ch-ua: "Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"' \

--header 'sec-ch-ua-mobile: ?0' \

--header 'sec-ch-ua-platform: "macOS"' \

--data '[

    {

        "addressType": "Postal",

        "popLabels": [

            "Billing"

        ],

        "preferenceTags": [

            {

                "type": "COMMUNICATION_PREFERENCE",

                "value": "DEFAULT",

                "attributes": {

                    "disallowedChannels": "SMS,CALL"

                }

            },

            {

                "type": "COMMUNICATION_PREFERENCE",

                "value": "CRITICAL",

                "attributes": {

                    "disallowedChannels": ""

                }

            },

            {

                "type": "COMMUNICATION_PREFERENCE",

                "value": "DIRECTED",

                "attributes": {

                    "disallowedChannels": ""

                }

            }

        ]

    },

    {

        "addressType": "Email",

        "popLabels": [

            "Communication"

        ],

        "preferenceTags": [

        

            {

                "type": "COMMUNICATION_PREFERENCE",

                "value": "ANNOUNCEMENT",

                "attributes": {

                    "disallowedChannels": ""

                }

            }

        ]

    }

]'
```

This API end point can be used to update communication preferences for a POP after a customer is onboarded.