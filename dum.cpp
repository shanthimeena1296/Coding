//REF from A3
int main(int argc, char *argv)
{
    int pipe1[2];
    int pipe2[2];
    pipe(pipe1);
    pipe(pipe2);
    //Process A
    pid child = fork();
    if(child == -1 )
    {
        std::cerr("Error:could not fork");
        return 1;
    }
    if(child == 0)
    {
        dup2(pipe1[1], STDOUT_FILENO);
        close(pipe1[0]);
        close(pipe1[1]);

        dup2(pipe2[0], STDIN_FILENO);
        close(pipe2[0]);
        close(pipe2[1]);

        exec(A);
    }
    //process B
    pid  child = fork();
    if(child == -1 )
    {
        std::cerr("Error:could not fork");
        return 1;
    }
    if(child == 0)
    {
        dup2(pipe2[1]), STDOUT_FILENO);
        close(pipe2[0]);
        close(pipe2[1]);

        dup2(pipe1[0]), STDIN_FILENO);
        close(pipe1[0]);
        close(pipe1[1]);

        exec(B);
    }

}