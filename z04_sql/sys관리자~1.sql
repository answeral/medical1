alter session set "_ORACLE_SCRIPT"=true;
--사용자 생성 "" 있으면 안됨.
create user ora_user identified by 1111;
--권한 부여
grant connect, resource, dba to ora_user;
--계정삭제
drop user "ora_user";

drop user "ora_user1";

drop user ora_user;

--권한삭제

revoke connect, resource, dba from ora_user;