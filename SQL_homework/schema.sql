drop table if exists "department_employee";
drop table if exists "department_manager";
drop table if exists "Salaries";
drop table if exists "Titles";
drop table if exists "Departments";
drop table if exists "Employees";

-- Create tables


CREATE TABLE "Departments" (
    "id" varchar   NOT NULL,
    "department_name" varchar   NOT NULL,
    CONSTRAINT "pk_Departments" PRIMARY KEY (
        "id"
     )
);

CREATE TABLE "department_employee" (
    "employee_id" integer   NOT NULL,
    "department_id" varchar   NOT NULL,
    "start_date" varchar   NOT NULL,
    "end_date" varchar   NOT NULL
);

CREATE TABLE "department_manager" (
    "department_id" varchar   NOT NULL,
    "employee_id" integer   NOT NULL,
    "start_date" varchar   NOT NULL,
    "end_date" varchar   NOT NULL
);

CREATE TABLE "Employees" (
    "id" integer   NOT NULL,
    "birth_date" varchar   NOT NULL,
    "first_name" varchar   NOT NULL,
    "last_name" varchar   NOT NULL,
    "gender" varchar   NOT NULL,
    "hire_date" varchar   NOT NULL,
    CONSTRAINT "pk_Employees" PRIMARY KEY (
        "id"
     )
);

CREATE TABLE "Salaries" (
    "employee_id" integer   NOT NULL,
    "salary" varchar   NOT NULL,
    "start_date" varchar   NOT NULL,
    "end_date" varchar   NOT NULL
);

CREATE TABLE "Titles" (
    "employee_id" integer   NOT NULL,
    "job_title" varchar   NOT NULL,
    "start_date" varchar   NOT NULL,
    "end_date" varchar   NOT NULL
);

-- Foreign key relations
ALTER TABLE "department_employee" ADD CONSTRAINT "fk_department_employee_employee_id" FOREIGN KEY("employee_id")
REFERENCES "Employees" ("id");

ALTER TABLE "department_employee" ADD CONSTRAINT "fk_department_employee_department_id" FOREIGN KEY("department_id")
REFERENCES "Departments" ("id");

ALTER TABLE "department_manager" ADD CONSTRAINT "fk_department_manager_department_id" FOREIGN KEY("department_id")
REFERENCES "Departments" ("id");

ALTER TABLE "department_manager" ADD CONSTRAINT "fk_department_manager_empoyee_id" FOREIGN KEY("empoyee_id")
REFERENCES "Employees" ("id");

ALTER TABLE "Salaries" ADD CONSTRAINT "fk_Salaries_employee_id" FOREIGN KEY("employee_id")
REFERENCES "Employees" ("id");

ALTER TABLE "Titles" ADD CONSTRAINT "fk_Titles_employee_id" FOREIGN KEY("employee_id")
REFERENCES "Employees" ("id");