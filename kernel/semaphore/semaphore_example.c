#include <linux/module.h>
#include <linux/semaphore.h>
#include <linux/kthread.h>
#include <linux/delay.h>

static struct semaphore mineral_sem;
static int mineral = 10;
static struct task_struct *zerg_thread;
static struct task_struct *terran_thread;

int mining_thread_function(void *data) {
    char *thread_name = (char *)data;

    while (1) {
        // 세마포어 획득 시도
        if (down_interruptible(&mineral_sem) != 0) {
            // 인터럽트 발생 시 종료
            break;
        }

        if (mineral > 0) {
            mineral--; // 공유 자원 사용
            printk(KERN_INFO "%s mined a mineral. Minerals left: %d\n", thread_name, mineral);
            msleep(1000);  // 1초 대기를 시뮬레이션합니다.
        } else {
            // 더 이상 채굴할 미네랄이 없으면 세마포어 반환
            up(&mineral_sem);
            break;
        }

        // 세마포어 반환
        up(&mineral_sem);
        schedule(); // 다른 스레드에 CPU 양보
    }

    return 0;
}

static int __init semaphore_example_init(void) {
    printk(KERN_INFO "Loaded semaphore_example module\n");

    // 세마포어 초기화
    sema_init(&mineral_sem, 1); // 세마포어를 1로 초기화하여 뮤텍스처럼 동작하도록 함

    // 커널 스레드 생성 및 실행
    zerg_thread = kthread_run(mining_thread_function, "zerg_drone", "zerg_thread");
    terran_thread = kthread_run(mining_thread_function, "terran_scv", "terran_thread");

    return 0;
}

static void __exit semaphore_example_exit(void) {
    printk(KERN_INFO "Unloaded semaphore_example module\n");
    // 생성된 커널 스레드 종료
    if (zerg_thread) {
        kthread_stop(zerg_thread);
    }
    if (terran_thread) {
        kthread_stop(terran_thread);
    }
}

module_init(semaphore_example_init);
module_exit(semaphore_example_exit);

MODULE_LICENSE("GPL");
MODULE_AUTHOR("Your Name");
MODULE_DESCRIPTION("Semaphore example with a shared resource in a Linux kernel module");
