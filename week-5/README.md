# Week-5

### 要求三

INSERT INTO member <br>
    -> VALUES ('001', 'Apple', 'test', 'test', '100', '2022-01-01');

INSERT INTO member VALUES ('002', 'Bobby', 'test', 'test', '200', '2022-07-01'),<br>
    -> ('003', 'Calvin', 'test', 'test', '300', '2022-12-01'),<br>
    -> ('004', 'David', 'test', 'test', '400', '2021-02-01'),<br>
    -> ('005', 'Eric', 'test', 'test', '500', '2020-07-07');

SELECT * FROM member;

![GITHUB](files/cmd-1.png)

mysql> SELECT * FROM member ORDER BY time DESC;

![GITHUB](files/cmd-2.png)

mysql> SELECT * FROM member ORDER BY time DESC LIMIT 1, 3;

![GITHUB](files/cmd-3.png)

mysql> SELECT * FROM member where username = 'test';

![GITHUB](files/cmd-4.png)

mysql> SELECT * FROM member where username = 'test' and password = 'test';

![GITHUB](files/cmd-5.png)

mysql> UPDATE member SET name = 'test2' where username = 'test';

![GITHUB](files/cmd-6.png)

### 要求四

mysql> SELECT count(*) from member;

![GITHUB](files/cmd-7.png)

mysql> SELECT sum(follower_count) from member;

![GITHUB](files/cmd-8.png)

mysql> SELECT avg(follower_count) from member;

![GITHUB](files/cmd-9.png)

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

INSERT INTO message (member_id, content, like_count) <br>
    -> VALUES (001, 'I am 001', 1);

INSERT INTO message (member_id, content, like_count)<br>
    -> VALUES (002, 'I am 002', 2),<br>
    -> (003, 'I am 003', 3),<br>
    -> (004, 'I am 004', 4),<br>
    -> (005, 'I am 005', 5);

SELECT mess.content, mem.name from message mess inner join member mem on mess.member_id = mem.id;


![GITHUB](files/cmd-10.png)

SELECT mess.content, mem.name from message mess inner join member mem on mess.member_id = mem.id where mem.username = 'test';

![GITHUB](files/cmd-11.png)

SELECT avg(mess.like_count) from message mess inner join member mem on mess.member_id = mem.id where mem.username = 'test';

![GITHUB](files/cmd-12.png)
