---
title: "Two way notification Integration with FRM for CardWorks: Contract - Orcus"
source: "https://zeta-tm.atlassian.net/wiki/spaces/ORCUS/pages/3456008473/Two+way+notification+Integration+with+FRM+for+CardWorks+Contract"
author:
published:
created: 2026-09-18
description:
tags:
  - "clippings"
---
## Two way notification Integration with FRM for CardWorks: Contract

## Objective

For Cardworks, each **successfully authorised** and **completed** transaction **will be sent to FS again in the CardNRT API** request.

The **CardRT** response will include a tag labeled "FOLLOW UP" for transactions that require validation as part of the Post Approval Risk Assessment.

When the **CardNRT** event request is sent from Orcus, for transactions where the **CardRT** response contains the tag "FOLLOW UP," a new attribute **msgStatusReason** as **FOLLOWUP** will be added to the **CardNRT** event during the FS invocation.

**NRT Response from the FS will have Queue Tag with the Action that needs to be taken against the user.**

**Based on the Queue Tag take actions for the txns.** For 2WAYNOTI we need to send the notification to the customer asking to approve / decline the txn.

Open Screenshot 2024-10-21 at 12.32.45 PM.png ![Screenshot 2024-10-21 at 12.32.45 PM.png](https://media-cdn.atlassian.com/file/94416c59-4f89-4111-81eb-a6f10f2f37e9/image/cdn?allowAnimated=true&client=2a4e2cc2-e7ec-4c58-981e-350986640e9d&collection=contentId-3456008473&height=125&max-age=2592000&mode=full-fit&source=mediaCard&token=eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiIyYTRlMmNjMi1lN2VjLTRjNTgtOTgxZS0zNTA5ODY2NDBlOWQiLCJhY2Nlc3MiOnsidXJuOmZpbGVzdG9yZTpjb2xsZWN0aW9uOmNvbnRlbnRJZC0zNDU2MDA4NDczIjpbInJlYWQiXX0sImV4cCI6MTc4OTcyNTI2MywibmJmIjoxNzg5NzIyMzgzLCJhYUlkIjoiNzEyMDIwOmIzMTRhNTYzLTY5NjYtNDJmNC05YjI2LWJkMzg3M2YyNGY3ZSIsImh0dHBzOi8vaWQuYXRsYXNzaWFuLmNvbS9hcHBBY2NyZWRpdGVkIjpmYWxzZSwiYXV0aFR5cGUiOiJzZXNzaW9uIn0.IEAJLOuJuPw8WyJJdhxF5ZQ25rUeiVsjTPIiE3NMCHk&width=612#media-blob-url=true&id=94416c59-4f89-4111-81eb-a6f10f2f37e9&clientId=2a4e2cc2-e7ec-4c58-981e-350986640e9d&contextId=contentId-3456008473&collection=contentId-3456008473)

Risk Evaluation Flow for CW

## Solution

For the `2WAYNOTI` action tag, make a call to **Luminous**, which will initiate a workflow to send the notification to the user.  

Open Untitled (1).png ![Untitled (1).png](https://media-cdn.atlassian.com/file/ba1d6cbd-bcdf-49a4-906f-60a162533463/image/cdn?allowAnimated=true&client=2a4e2cc2-e7ec-4c58-981e-350986640e9d&collection=contentId-3456008473&height=125&max-age=2592000&mode=full-fit&source=mediaCard&token=eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiIyYTRlMmNjMi1lN2VjLTRjNTgtOTgxZS0zNTA5ODY2NDBlOWQiLCJhY2Nlc3MiOnsidXJuOmZpbGVzdG9yZTpjb2xsZWN0aW9uOmNvbnRlbnRJZC0zNDU2MDA4NDczIjpbInJlYWQiXX0sImV4cCI6MTc4OTcyNTI2MywibmJmIjoxNzg5NzIyMzgzLCJhYUlkIjoiNzEyMDIwOmIzMTRhNTYzLTY5NjYtNDJmNC05YjI2LWJkMzg3M2YyNGY3ZSIsImh0dHBzOi8vaWQuYXRsYXNzaWFuLmNvbS9hcHBBY2NyZWRpdGVkIjpmYWxzZSwiYXV0aFR5cGUiOiJzZXNzaW9uIn0.IEAJLOuJuPw8WyJJdhxF5ZQ25rUeiVsjTPIiE3NMCHk&width=760#media-blob-url=true&id=ba1d6cbd-bcdf-49a4-906f-60a162533463&clientId=2a4e2cc2-e7ec-4c58-981e-350986640e9d&contextId=contentId-3456008473&collection=contentId-3456008473)

Queue Tag Processing Flow

Open Untitled.png ![Untitled.png](https://media-cdn.atlassian.com/file/71116720-b568-4701-8199-d97b45158f76/image/cdn?allowAnimated=true&client=2a4e2cc2-e7ec-4c58-981e-350986640e9d&collection=contentId-3456008473&height=125&max-age=2592000&mode=full-fit&source=mediaCard&token=eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiIyYTRlMmNjMi1lN2VjLTRjNTgtOTgxZS0zNTA5ODY2NDBlOWQiLCJhY2Nlc3MiOnsidXJuOmZpbGVzdG9yZTpjb2xsZWN0aW9uOmNvbnRlbnRJZC0zNDU2MDA4NDczIjpbInJlYWQiXX0sImV4cCI6MTc4OTcyNTI2MywibmJmIjoxNzg5NzIyMzgzLCJhYUlkIjoiNzEyMDIwOmIzMTRhNTYzLTY5NjYtNDJmNC05YjI2LWJkMzg3M2YyNGY3ZSIsImh0dHBzOi8vaWQuYXRsYXNzaWFuLmNvbS9hcHBBY2NyZWRpdGVkIjpmYWxzZSwiYXV0aFR5cGUiOiJzZXNzaW9uIn0.IEAJLOuJuPw8WyJJdhxF5ZQ25rUeiVsjTPIiE3NMCHk&width=760#media-blob-url=true&id=71116720-b568-4701-8199-d97b45158f76&clientId=2a4e2cc2-e7ec-4c58-981e-350986640e9d&contextId=contentId-3456008473&collection=contentId-3456008473)

notification-response processor

Sequence Diagram: [FRM 2WayNotification SequenceDiagram](https://docs.google.com/document/d/1ZOYHNjtbcUd50ygR0iJIXc1KzEuxB4SCdVk31puZ3Fk/edit?usp=sharing)

[Summarise](https://docs.google.com/document/d/1ZOYHNjtbcUd50ygR0iJIXc1KzEuxB4SCdVk31puZ3Fk/edit?usp=sharing)

Sub1: `_orcus_code_interceptor_featurespace_switch-authorization_600309_RESOURCE`

Sub2: `_orcus_code_interceptor_featurespace_queueTag-processor_600309_orcus-transactions`

## Payload to be Sent to Luminous for Triggering Notification Workflow

```
POST /1.0/tenants/{tenantID}/workflows/{workflowType}/initiate 

--data-raw {

  "eventData": {

    "accountHolderId": "abf41be6-8d6d-4ed6-8c1f-d9f83f28cec4",

    "transactionId": "CGC03IN5U1022",

    "cguid": "b8dc00c9-3331-4ac7-8694-6587b1fcc121",

    "maskedPAN": "999999-xxxxxx-3629",

    "merchantName": "AMAZON",

    "transactionAmount": {

      "value": 30.0,

      "currency": "USD",

      "baseValue": 30.0,

      "baseCurrency": "USD"

    },

    "timestamp": 1729789673,

    "tenantId": 600335,

    "action": "TWO_WAY_NOTIFICATION",

    "triggeredRule": "RULE_1,RULE_2",

    "valueTime": "2024-10-22T10:11:09.184Z",

    "rrn": "429610835279",

    "resourceID": "d422a0fe-2b76-4b9a-8839-13e82a6961a1"

  }

}
```

WorkflowType: `CWFRMWorkflow` for CardWorks Workflow on FRM.

Sandbox details to call `POST /initiate` API

Refer: [Notification Workflow Contracts with Orcus/FRM](https://zeta-tm.atlassian.net/wiki/x/E4ITzQ)

Once Luminous gets response from the Customer, it publishes event to `notificationWorkflowResponse` topic, Orcus would create a Subscription for this topic and take action(Account Block / no action) based on the customer response

Refer: [2 Way Notification Integration - Solutioning.docx](https://zetaworld-my.sharepoint.com/:w:/r/personal/abhinava_zeta_tech/Documents/2%20Way%20Notification%20Integration%20-%20Solutioning.docx?d=w687e5a2c731347a5b194481a00d8b992&csf=1&web=1&e=ntQxnn "https://zetaworld-my.sharepoint.com/:w:/r/personal/abhinava_zeta_tech/Documents/2%20Way%20Notification%20Integration%20-%20Solutioning.docx?d=w687e5a2c731347a5b194481a00d8b992&csf=1&web=1&e=ntQxnn")