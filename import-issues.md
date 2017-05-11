
```
Error importing data: org.xml.sax.SAXException: com.atlassian.jira.exception.DataAccessException:
org.ofbiz.core.entity.GenericEntityException: while inserting: [GenericEntity:Action][updateauthor,steven.wang][issue,13273][author,steven.wang][created,2015-07-07 12:44:31.0][id,12724][type,comment][body,|| No. || API || COUNT（41） || DONE（38） || | 1 | user | 15 | 15 | | 2 | signature | 5 | 4 | | 3 | template | 12 | 12 | | 4 | document | 6 | 4 | | 5 | certificate | 3 | 3 |][updated,2015-07-23 14:54:26.0]
(SQL Exception while executing the following:
  INSERT INTO jiraaction (ID, issueid, AUTHOR, actiontype, actionlevel, rolelevel, actionbody, CREATED, UPDATEAUTHOR, UPDATED, actionnum) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) (Incorrect string value: '\xEF\xBC\x8841\xEF...' for column 'actionbody' at row 1))
  java.lang.Exception: com.atlassian.jira.exception.DataAccessException:
  org.ofbiz.core.entity.GenericEntityException:
  while inserting: [GenericEntity:Action][updateauthor,steven.wang][issue,13273][author,steven.wang][created,2015-07-07 12:44:31.0][id,12724][type,comment][body,|| No. || API || COUNT（41） || DONE（38） || | 1 | user | 15 | 15 | | 2 | signature | 5 | 4 | | 3 | template | 12 | 12 | | 4 | document | 6 | 4 | | 5 | certificate | 3 | 3 |][updated,2015-07-23 14:54:26.0] (SQL Exception while executing the following:INSERT INTO jiraaction (ID, issueid, AUTHOR, actiontype, actionlevel, rolelevel, actionbody, CREATED, UPDATEAUTHOR, UPDATED, actionnum) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) (Incorrect string value: '\xEF\xBC\x8841\xEF...' for column 'actionbody' at row 1))
```

solution:

ALTER DATABASE jira CHARACTER SET utf8 COLLATE utf8_unicode_ci;
