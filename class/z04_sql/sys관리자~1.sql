alter session set "_ORACLE_SCRIPT"=true;
--����� ���� "" ������ �ȵ�.
create user ora_user identified by 1111;
--���� �ο�
grant connect, resource, dba to ora_user;
--��������
drop user "ora_user";

drop user "ora_user1";

drop user ora_user;

--���ѻ���

revoke connect, resource, dba from ora_user;