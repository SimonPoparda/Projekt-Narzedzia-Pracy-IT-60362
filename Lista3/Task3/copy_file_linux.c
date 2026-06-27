#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <errno.h>
#include <string.h>

#define BUFFER_SIZE 4096

int main(int argc, char *argv[]) {
    if (argc != 3) {
        fprintf(stderr, "Usage: %s <source> <destination>\n", argv[0]);
        return 1;
    }

    const char *src = argv[1];
    const char *dst = argv[2];
    int src_fd, dst_fd;
    ssize_t bytes_read, bytes_written;
    char buffer[BUFFER_SIZE];

    // Open source file for reading
    src_fd = open(src, O_RDONLY);
    if (src_fd == -1) {
        perror("open (source)");
        return 1;
    }

    // Create/truncate destination file for writing
    dst_fd = open(dst, O_WRONLY | O_CREAT | O_TRUNC, 0644);
    if (dst_fd == -1) {
        perror("open (destination)");
        close(src_fd);
        return 1;
    }

    // Copy file in chunks
    while ((bytes_read = read(src_fd, buffer, BUFFER_SIZE)) > 0) {
        bytes_written = write(dst_fd, buffer, bytes_read);
        if (bytes_written != bytes_read) {
            perror("write");
            close(src_fd);
            close(dst_fd);
            return 1;
        }
    }

    if (bytes_read == -1) {
        perror("read");
        close(src_fd);
        close(dst_fd);
        return 1;
    }

    // Close files
    if (close(src_fd) == -1) {
        perror("close (source)");
        return 1;
    }

    if (close(dst_fd) == -1) {
        perror("close (destination)");
        return 1;
    }

    printf("File copied successfully: %s -> %s\n", src, dst);
    return 0;
}
