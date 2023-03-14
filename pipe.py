int main (int argc, char *argv) {

	std::vector<pid_t> kids;

	int pipe1[2];
	pipe(pipe1);

   
	int pipe2[2];
	pipe(pipe2);

	pid_t child_pid;

	child_pid = fork();
	if (child_pid == 0)
	{
		// standard output to pipe
		dup2(pipe1[1], STDOUT_FILENO);
		close(pipe1[0]);
		close(pipe1[1]);  
		
		return procRgen(argc,argv);
	}
    else if (child_pid<0){
        std::cerr<<"Error: could not fork\n";
        return 1;
    }

	kids.push_back(child_pid);
	
	child_pid = fork();
	if (child_pid == 0) {
		dup2(pipe1[0], STDIN_FILENO);
		close(pipe1[0]);
		close(pipe1[1]);

		dup2(pipe2[1], STDOUT_FILENO);
		close(pipe2[0]);
		close(pipe2[1]);

		return procA1(argc,argv);
	}
    else if (child_pid<0){
        std::cerr<<"Error: could not fork\n";
        return 1;
    }

	kids.push_back(child_pid);

	child_pid = fork();
	if (child_pid == 0)
	{
        //redirect stdin from pipe
		dup2(pipe2[0], STDIN_FILENO);
		close(pipe2[1]);
		close(pipe2[0]);

		return procA2(argc, argv);

	}
    else if(child_pid<0)
    {
        std::cerr<<"Error: could not fork\n";
        return 1;
    }

	kids.push_back(child_pid);
	child_pid = 0;
    child_pid = fork();
    if(child_pid==0){
        dup2(pipe2[1], STDOUT_FILENO);
	close(pipe2[0]);
	close(pipe2[1]);

    
	int res = procInput();
    return 0;    
    }
    kids.push_back(child_pid);

    int waitforChild;
    wait(&waitforChild);

    for (pid_t k : kids) {

        int status;

        kill (k, SIGTERM);

        waitpid(k, &status, 0);

    }
	return 0;
}