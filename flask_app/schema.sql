create table if not exists events (
    headline text not null,
    blurb text not null,
    description text not null,
    time real not null,
    images blob
);
create table if not exists research (
    headline text not null,
    blurb text not null,
    description text not null,
    time real not null,
    images blob
);
create table if not exists people (
    name text not null,
    blurb text not null,
    description text not null,
    time real not null,
    images blob
);
create table if not exists resources (
    headline text not null,
    blurb text not null,
    description text not null,
    time real not null,
    images blob
);