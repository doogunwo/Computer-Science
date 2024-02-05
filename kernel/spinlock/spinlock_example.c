#include <linux/module.h>
#include <linux/spinlock.h> //스핀락 사용하기 위한 헤더
#include <linux/sched.h>
#include <linux/kthread.h>
#include <linux/delay.h>

static DEFINE_SPINLOCK(mineral_lock);
static int mineral = 10;
static struct task_struct *zerg_thread;
static struct task_struct *terran_thread;

int mining_thread_function(void *data) {
    unsigned long flags;
    char *thread_name = (char *)data;//스레드 이름
    //스레드 종료 요청이 있을 때 까지 반복
    while (!kthread_should_stop()) {
        spin_lock_irqsave(&mineral_lock, flags);
        //스핀락 획득 및 인터럽트 상태 저장
        if (mineral > 0) {
            mineral--;
            printk(KERN_INFO "%s mined a mineral. Minerals left: %d\n", thread_name, mineral);
            msleep(1000);  // 1초 기다리기
        } else {//채굴할 미네랄 없으면 스핀락 해제 및 종료
            spin_unlock_irqrestore(&mineral_lock, flags);
            break;
        }
        //스핀락 해제 및 인터럽트 복원
        spin_unlock_irqrestore(&mineral_lock, flags);
        schedule();//다른 스레드에 cpu 양보
    }

    return 0;
}

static int __init spinlock_example_init(void) {
    printk(KERN_INFO "Loaded spinlock_example module\n");
    //커널 스레드 생성 2개 각각 저그와 테란
    zerg_thread = kthread_run(mining_thread_function, "zerg_drone", "zerg_thread");
    terran_thread = kthread_run(mining_thread_function, "terran_scv", "terran_thread");

    return 0;
}

static void __exit spinlock_example_exit(void) {
    printk(KERN_INFO "Unloaded spinlock_example module\n");
    if (zerg_thread) {// 생성된 스레드 각각 종료
        kthread_stop(zerg_thread);
    }
    if (terran_thread) {
        kthread_stop(terran_thread);
    }
}

module_init(spinlock_example_init);
module_exit(spinlock_example_exit);

MODULE_LICENSE("GPL");
MODULE_AUTHOR("doogunwo");
MODULE_DESCRIPTION("Spinlock example with a shared resource in a Linux kernel module");
