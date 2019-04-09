violin_dual

rviz code: roslaunch violin_description violin_dual_arm_publisher.launch
gazebo code: roslaunch violin_dual_gazebo violin_dual_arm_world.launch
             
execute code: roslaunch violin_dual_arm_bringup dual_arm_bringup.launch
              roslaunch violin_dual_moveit_configuration violin_dual_moveit_planning_execution.launch 
   

http://docs.ros.org/indigo/api/pr2_moveit_tutorials/html/planning/src/doc/move_group_interface_tutorial.html#dual-arm-pose-goals

  1. violin_description
    1.1. launch
        - violin_dual_arm_publisher.launch: 
                작성한 xacro를 urdf로 바꿔주는 param이 있음(line 2)
                로봇의 작동범위를 파악하기 위해 robot_state_publisher 및 joint_state_publisher가 포함되어 있음(line 3-6)
             launch 실행 시, 자동으로 rviz 프로그램을 띄울 수 있도록 코드 삽입 됨(line 9).

    1.2. meshes
        - violin robot의 몸통 stl 파일이 저장되어있는 폴더.

    1.3. urdf
        - violin_dual_arm_v1.xacro:
                로봇 몸통과 ur3 팔 두개를 이어붙힌 최종 xacro 파일. ur3의 xacro를 이용하기 때문에 universal robot의 패키지를 설치 해야 사용 가능.  
        - l_ur3_joint_limited_robot.urdf.xacro:
                로봇의 왼쪽 팔. 역시 xacro를 이용함. universal robot의 패키지에 있는 xacro 파일을 include 하는 구문이 있다.
        - r_ur3_joint_limited_robot.urdf.xacro:
                로봇의 오른 팔. 역시 xacro를 이용함. universal robot의 패키지에 있는 xacro 파일을 include 하는 구문이 있다.


   2. violin_dual_gazebo
     2.1. controller
        - joint_state_controller.yaml:
            safe_arm과 비교할 경우, "safe_arm_joint_state.yaml와 같은 파일.'
        - l_arm_controller_dual.yaml: 
            왼쪽 팔의 joint 요소들이 적혀 있음.
        - r_arm_controller_dual.yaml:
            오른쪽 팔의 joint 요소들이 적혀 있음.

     2.2. launch
        - controller_utils.launch:
            현재는 안쓰임(2018.02.21)
        - dual_arm_joint_state_controller.launch:
            robot_state publisher와 joint_state_controller를 불러오는 부분
        - dual_arm_l_controller.launch:
            왼쪽팔의 controller 정의.
        - dual_arm_r_controller.launch:
            오른쪽 팔의 controller 정의  
        - dual_arm.launch:
            현재는 안쓰임(2018.02.21)                  
        - violin_dual_arm_world.launch:
            로봇 몸통과 ur3 팔 두개를 이어붙힌 가제보 시뮬레이션 월드
        
     2.3. worlds
        - violin_dual_arm.world: 
            "violin_dual_arm_world.launch"에서 필요한 기본 월드가 작성되어 있는 파일


   3. violin_dual_arm_bringup: ros_control과 gazebo를 결합시킨 패키지
     3.1. launch
        - dual_arm_bringup.launch:
            gazebo 시뮬레이션과 ros_control을 결합시킨 패키지. 실행 시 gazebo가 켜지면서 dual_arm의 joint_state 등을 불러온다.


   4. violin_dual_moveit_configuration
     4.1. config
        - controllers.yaml: 
            moveit!으로 생성된 로봇의 팔 control 요소를 적은 곳. 이때, name 파라미터는 l_arm_controller_dual.yaml, r_arm_controller_dual.yaml 와 일치시켜야함.    
                


