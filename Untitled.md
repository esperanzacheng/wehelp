# Week-5

### 要求三

INSERT INTO member <br>
    -> VALUES ('001', 'Apple', 'test', 'test', '100', '2022-01-01');

INSERT INTO member VALUES ('002', 'Bobby', 'test', 'test', '200', '2022-07-01'),<br>
    -> ('003', 'Calvin', 'test', 'test', '300', '2022-12-01'),<br>
    -> ('004', 'David', 'test', 'test', '400', '2021-02-01'),<br>
    -> ('005', 'Eric', 'test', 'test', '500', '2020-07-07');

SELECT * FROM member;

![cmd-1.png](attachment:cmd-1.png)

mysql> SELECT * FROM member ORDER BY time DESC;

![cmd-2.png](attachment:cmd-2.png)

mysql> SELECT * FROM member ORDER BY time DESC LIMIT 1, 3;

![cmd-3.png](attachment:cmd-3.png)

mysql> SELECT * FROM member where username = 'test';

![cmd-4-2.png](attachment:cmd-4-2.png)

mysql> SELECT * FROM member where username = 'test' and password = 'test';

![cmd-5.png](attachment:cmd-5.png)

mysql> UPDATE member SET name = 'test2' where username = 'test';

![cmd-6.png](attachment:cmd-6.png)

### 要求四

mysql> SELECT count(*) from member;

![cmd-7.png](attachment:cmd-7.png)

mysql> SELECT sum(follower_count) from member;

![cmd-8.png](attachment:cmd-8.png)

mysql> SELECT avg(follower_count) from member;

![cmd-9.png](attachment:cmd-9.png)

### 要求五

CREATE TABLE message ( <br>
    -> id bigint AUTO_INCREMENT, <br>
    -> member_id bigint NOT NULL,<br>
    -> content varchar(255) NOT NULL,<br>
    -> like_count int unsigned NOT NULL DEFAULT 0,<br>
    -> time datetime NOT NULL DEFAULT NOW(),<br>
    -> PRIMARY KEY(id),<br>
    -> FOREIGN KEY (member_id) REFERENCES member(id)<br>
    -> );


