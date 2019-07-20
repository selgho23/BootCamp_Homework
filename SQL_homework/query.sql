-- Check for successful data import
select * from "Departments";
select * from "Employees";
select * from "Salaries";
select * from "Titles";
select * from "department_employee";
select * from "department_manager";

-- List of employee number, last name, first name, gender, and salary
select s.employee_id, e.last_name, e.first_name, e.gender, s.salary
from "Employees" as e
inner join "Salaries" as s
	on s.employee_id = e.id
	
-- List of employees who were hired in 1986
select * from "Employees"
where hire_date like '1986%'

-- List of the manager of each department with ...
-- ... department number, department name, employee number
-- ... last name, first name, start and end employment dates
select dm.department_id, d.department_name, dm.employee_id, e.last_name,
	   e.first_name, dm.start_date, dm.end_date
from "Departments" as d 
right join "department_manager" as dm
	on d.id = dm.department_id
left join "Employees" as e
	on e.id = dm.employee_id
	
-- List of the department of each employee with ...
-- ... employee number, last name, first name, and department name
select de.employee_id, e.last_name, e.first_name, d.department_name
from "Employees" as e
right join "department_employee" as de
	on e.id = de.employee_id
left join "Departments" as d
	on d.id = de.department_id
	
-- List of all employees whose first name is Hercules and last names 
-- begin with B
select * from "Employees" 
where first_name = 'Hercules' and last_name like 'B%'

-- List of all employees in the Sales department with ...
-- ... employee number, last name, first name, department name
select de.employee_id, e.last_name, e.first_name, d.department_name
from "Employees" as e
right join "department_employee" as de
	on e.id = de.employee_id
left join "Departments" as d
	on d.id = de.department_id
where d.department_name = 'Sales'

-- List of all employees in the Sales and Development departments with ...
-- ... employee number, last name, first name, department name
select de.employee_id, e.last_name, e.first_name, d.department_name
from "Employees" as e
right join "department_employee" as de
	on e.id = de.employee_id
left join "Departments" as d
	on d.id = de.department_id
where d.department_name = 'Sales' or d.department_name = 'Development'

-- Frequency count of employee last names, in descending order
select last_name, count(last_name) as "Frequency of Last Name"
from "Employees"
group by last_name
order by "Frequency of Last Name" desc


