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