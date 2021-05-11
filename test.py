import log
import get_time

act1 = log.make_activity('homework', get_time.get_time(), get_time.get_time())
act2 = log.make_activity('the secret to the krabby patty formula is putting pooo in the sauce', '10:30:00', '12:45:30')

my_list = []


my_list = log.add_activity(my_list, act1)
my_list = log.add_activity(my_list, act2)

log.print_log(my_list)

