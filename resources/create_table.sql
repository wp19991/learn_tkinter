drop table if exists `user`;
create table `user`
(
    `gmt_create`   datetime     not null,
    `gmt_modified` datetime     not null,

    `user_name`    varchar(255) not null,
    `password`     varchar(255) not null default '123456',
    constraint web_password_table_pk
        primary key (user_name)
);

drop table if exists `web_password`;
create table `web_password`
(
    `gmt_create`   datetime     not null,
    `gmt_modified` datetime     not null,

    `web_name`     varchar(255) not null,
    `account`      varchar(255) not null,
    `password`     varchar(255) not null default '',
    constraint web_password_table_pk
        primary key (web_name, account)
);