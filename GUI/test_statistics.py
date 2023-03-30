

import plam_det
import json
import tr_dis



def test_statisics_init(widgets):
    # TEST STATISTICS
    plam_det.log_display(widgets,'Test statistics init...')
    print('Test statistics init...')
    try:
        with open('./test/test_statistics.json', 'r') as f:
            test_data = json.load(f)

        widgets.left_test_count.setText(test_data['test_data']['left_box']['total_count'])
        widgets.left_pass_count.setText(test_data['test_data']['left_box']['pass_count'])
        widgets.left_fail_count.setText(test_data['test_data']['left_box']['fail_count'])
        widgets.left_fail_rate.setText(test_data['test_data']['left_box']['fail_rate'])

        widgets.right_test_count.setText(test_data['test_data']['right_box']['total_count'])
        widgets.right_pass_count.setText(test_data['test_data']['right_box']['pass_count'])
        widgets.right_fail_count.setText(test_data['test_data']['right_box']['fail_count'])
        widgets.right_fail_rate.setText(test_data['test_data']['right_box']['fail_rate'])

    except:
        plam_det.log_display(widgets,'Test data load error!')
        print('Test data load error!')
        return False
    else:
        plam_det.log_display(widgets,'Test statistics complete!')
        print('Test statistics complete!')
        return test_data
    

def test_statisics_save(widgets, channel, result):
    plam_det.log_display(widgets,'Test statistics save...')
    print('Test statistics save...')

    try:
        with open('./test/test_statistics.json', 'r') as f:
            test_data = json.load(f)
        
        if result == 'pass':
            if channel == 'left':
                test_data['test_data']['left_box']['pass_count'] = str(int(test_data['test_data']['left_box']['pass_count']) + 1)
                test_data['test_data']['left_box']['total_count'] = str(int(test_data['test_data']['left_box']['total_count']) + 1)
                test_data['test_data']['left_box']['fail_rate'] = str(round(int(test_data['test_data']['left_box']['fail_count']) / int(test_data['test_data']['left_box']['total_count']), 2))

                widgets.left_test_count.setText(test_data['test_data']['left_box']['total_count'])
                widgets.left_pass_count.setText(test_data['test_data']['left_box']['pass_count'])
                widgets.left_fail_count.setText(test_data['test_data']['left_box']['fail_count'])
                widgets.left_fail_rate.setText(test_data['test_data']['left_box']['fail_rate'])
            
            elif channel == 'right':
                test_data['test_data']['right_box']['pass_count'] = str(int(test_data['test_data']['right_box']['pass_count']) + 1)
                test_data['test_data']['right_box']['total_count'] = str(int(test_data['test_data']['right_box']['total_count']) + 1)
                test_data['test_data']['right_box']['fail_rate'] = str(round(int(test_data['test_data']['right_box']['fail_count']) / int(test_data['test_data']['right_box']['total_count']), 2))
        
                widgets.right_test_count.setText(test_data['test_data']['right_box']['total_count'])
                widgets.right_pass_count.setText(test_data['test_data']['right_box']['pass_count'])
                widgets.right_fail_count.setText(test_data['test_data']['right_box']['fail_count'])
                widgets.right_fail_rate.setText(test_data['test_data']['right_box']['fail_rate'])

        elif result == 'fail':
            if channel == 'left':
                test_data['test_data']['left_box']['fail_count'] = str(int(test_data['test_data']['left_box']['fail_count']) + 1)
                test_data['test_data']['left_box']['total_count'] = str(int(test_data['test_data']['left_box']['total_count']) + 1)
                test_data['test_data']['left_box']['fail_rate'] = str(round(int(test_data['test_data']['left_box']['fail_count']) / int(test_data['test_data']['left_box']['total_count']), 2))
            
                widgets.left_test_count.setText(test_data['test_data']['left_box']['total_count'])
                widgets.left_pass_count.setText(test_data['test_data']['left_box']['pass_count'])
                widgets.left_fail_count.setText(test_data['test_data']['left_box']['fail_count'])
                widgets.left_fail_rate.setText(test_data['test_data']['left_box']['fail_rate'])
                

            elif channel == 'right':
                test_data['test_data']['right_box']['fail_count'] = str(int(test_data['test_data']['right_box']['fail_count']) + 1)
                test_data['test_data']['right_box']['total_count'] = str(int(test_data['test_data']['right_box']['total_count']) + 1)
                test_data['test_data']['right_box']['fail_rate'] = str(round(int(test_data['test_data']['right_box']['fail_count']) / int(test_data['test_data']['right_box']['total_count']), 2))

                widgets.right_test_count.setText(test_data['test_data']['right_box']['total_count'])
                widgets.right_pass_count.setText(test_data['test_data']['right_box']['pass_count'])
                widgets.right_fail_count.setText(test_data['test_data']['right_box']['fail_count'])
                
        with open('./test/test_statistics.json', 'w') as f:
            json.dump(test_data, f, indent=4)

    except:
        plam_det.log_display(widgets,'Test data save error!')
        print('Test data save error!')
        return False
    else:
        plam_det.log_display(widgets,'Test statistics save complete!')
        print('Test statistics save complete!')
        return True





