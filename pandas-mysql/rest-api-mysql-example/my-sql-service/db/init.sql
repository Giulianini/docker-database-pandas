USE my_db;

DROP TABLE IF EXISTS
    student;

-- Always snake_case convention because sql syntax is case unsensitive and make no sense to use Pascal/Camel/Upper case mix
CREATE TABLE university (
    university_id BIGINT(20) NOT NULL,
    name VARCHAR(255) DEFAULT NULL,
    -- Constraints
    PRIMARY KEY(university_id)
);

CREATE TABLE course (
    course_id BIGINT(20) NOT NULL,
    university_id BIGINT(20) NOT NULL,
    name VARCHAR(255) DEFAULT NULL,
    max_students INT(10) DEFAULT NULL,
    -- Costraints
    PRIMARY KEY(course_id),
    FOREIGN KEY(university_id) 
        REFERENCES university(university_id)
        ON DELETE CASCADE
);

CREATE TABLE student (
    student_id BIGINT(20) NOT NULL,
    course_id BIGINT(20) NOT NULL,
    name VARCHAR(255) DEFAULT NULL,
    surname VARCHAR(255) DEFAULT NULL,
    year INT(10) DEFAULT NULL,
    -- Costraints
    PRIMARY KEY(student_id),
    FOREIGN KEY(course_id)
        REFERENCES course(course_id)
        ON DELETE CASCADE
);

INSERT INTO university (university_id, name)
VALUES ('01', 'Unibo');