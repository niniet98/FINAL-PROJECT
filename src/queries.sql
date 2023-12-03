use linkedin;

-- Queries related with experience level relationship with remote_ratio
select experience_level, count(remote_ratio) count_remote from linkedin
	where remote_ratio = "En remoto" and experience_level is not null
	group by experience_level
	order by count_remote desc;

select experience_level, count(remote_ratio) count_hibrid from linkedin
    where remote_ratio = "Híbrido" and experience_level is not null
    group by experience_level
    order by count_hibrid desc;
    
select experience_level, count(remote_ratio) count_onsite from linkedin
    where remote_ratio = "Presencial" and experience_level is not null
    group by experience_level
    order by count_onsite desc;

-- Average salary by level of experience and type of employment
select employment_type, experience_level, round(avg(salary), 2) as avg_salary
from linkedin
where experience_level is not null
group by employment_type, experience_level
order by employment_type, experience_level;

-- Number of companies offering each job title with the minimun, average and maximum salary associated with each one
select job_title, count(company_name) as num_companies, 
	round(min(salary), 2) as min_salary,
    round(avg(salary), 2) as avg_salary,
    round(max(salary), 2) as max_salary
from linkedin
group by job_title
order by num_companies desc;

-- Relationship between job_title, company_size and its average salary
select job_title, company_size, round(avg(salary), 2) as avg_salary
from linkedin
where company_size is not null
group by job_title, company_size
order by job_title;



