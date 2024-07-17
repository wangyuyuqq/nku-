/*
 Navicat Premium Data Transfer

 Source Server         : project
 Source Server Type    : MySQL
 Source Server Version : 80036
 Source Host           : localhost:3306
 Source Schema         : emp_project

 Target Server Type    : MySQL
 Target Server Version : 80036
 File Encoding         : 65001

 Date: 02/06/2024 19:39:50
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for admin_login
-- ----------------------------
DROP TABLE IF EXISTS `admin_login`;
CREATE TABLE `admin_login`  (
  `admin_id` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `admin_pwd` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  PRIMARY KEY (`admin_id`) USING BTREE,
  CONSTRAINT `admin_login_ibfk_1` FOREIGN KEY (`admin_id`) REFERENCES `teacher` (`tea_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of admin_login
-- ----------------------------
INSERT INTO `admin_login` VALUES ('01001', '123456');

-- ----------------------------
-- Table structure for college
-- ----------------------------
DROP TABLE IF EXISTS `college`;
CREATE TABLE `college`  (
  `college_name` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `college_id` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`college_name`) USING BTREE,
  INDEX `manged_by`(`college_id` ASC) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of college
-- ----------------------------
INSERT INTO `college` VALUES ('人工智能学院', 'COS01');
INSERT INTO `college` VALUES ('电子信息与光学工程学院', 'COS02');
INSERT INTO `college` VALUES ('网络空间安全学院', 'COS03');
INSERT INTO `college` VALUES ('计算机学院', 'COS04');
INSERT INTO `college` VALUES ('软件学院', 'COS05');

-- ----------------------------
-- Table structure for learn
-- ----------------------------
DROP TABLE IF EXISTS `learn`;
CREATE TABLE `learn`  (
  `stu_id` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `lesson_id` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `score` float(255, 0) NULL DEFAULT NULL,
  `class_number` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`stu_id`, `lesson_id`) USING BTREE,
  INDEX `lesson`(`lesson_id` ASC) USING BTREE,
  CONSTRAINT `lesson` FOREIGN KEY (`lesson_id`) REFERENCES `lesson` (`lesson_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `stu` FOREIGN KEY (`stu_id`) REFERENCES `student` (`stu_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of learn
-- ----------------------------
INSERT INTO `learn` VALUES ('00001', '0107', 70, 'C321');
INSERT INTO `learn` VALUES ('00001', '0303', 99, 'C321');
INSERT INTO `learn` VALUES ('00001', '0911', 99, 'C321');
INSERT INTO `learn` VALUES ('00001', '1023', 100, 'E102');
INSERT INTO `learn` VALUES ('00001', '1025', 99, 'E105');
INSERT INTO `learn` VALUES ('00001', 'L007', 99, 'D103');
INSERT INTO `learn` VALUES ('00001', 'L009', 80, 'E109');
INSERT INTO `learn` VALUES ('00001', 'L010', 99, 'F180');
INSERT INTO `learn` VALUES ('00002', '0303', 78, 'C321');
INSERT INTO `learn` VALUES ('00002', '0911', 88, 'C321');
INSERT INTO `learn` VALUES ('00002', '1012', 92, 'C321');
INSERT INTO `learn` VALUES ('00003', '0911', 92, 'C321');
INSERT INTO `learn` VALUES ('00003', '1017', 80, 'D105');
INSERT INTO `learn` VALUES ('00003', '1023', 86, 'E102');
INSERT INTO `learn` VALUES ('00006', '1025', 75, 'E105');
INSERT INTO `learn` VALUES ('00006', '1031', 70, 'F102');
INSERT INTO `learn` VALUES ('00007', '1017', 95, 'D105');
INSERT INTO `learn` VALUES ('00008', '1329', 87, 'F130');
INSERT INTO `learn` VALUES ('00008', '3001', 91, 'W121');
INSERT INTO `learn` VALUES ('00009', '1023', 90, 'E102');
INSERT INTO `learn` VALUES ('00009', '3311', 85, 'C321');
INSERT INTO `learn` VALUES ('00010', '1025', 80, 'E105');
INSERT INTO `learn` VALUES ('00010', 'L002', 88, 'B309');
INSERT INTO `learn` VALUES ('00010', 'L003', 90, 'C121');
INSERT INTO `learn` VALUES ('00011', 'L004', 83, 'C122');
INSERT INTO `learn` VALUES ('00011', 'L005', 87, 'C123');
INSERT INTO `learn` VALUES ('00012', 'L006', 82, 'C321');
INSERT INTO `learn` VALUES ('00012', 'L007', 85, 'D103');
INSERT INTO `learn` VALUES ('00013', 'L008', 80, 'E103');
INSERT INTO `learn` VALUES ('00013', 'L009', 84, 'E109');
INSERT INTO `learn` VALUES ('00014', '0107', 100, 'C321');
INSERT INTO `learn` VALUES ('00014', 'L010', 81, 'F180');
INSERT INTO `learn` VALUES ('00015', '0303', 87, 'C321');
INSERT INTO `learn` VALUES ('00015', '0911', 90, 'C321');
INSERT INTO `learn` VALUES ('00016', '1012', 82, 'C321');
INSERT INTO `learn` VALUES ('00016', '1017', 86, 'D105');
INSERT INTO `learn` VALUES ('00017', '1023', 88, 'E102');
INSERT INTO `learn` VALUES ('00017', '1025', 91, 'E105');
INSERT INTO `learn` VALUES ('00018', '1031', 84, 'F102');
INSERT INTO `learn` VALUES ('00018', '1329', 89, 'F130');

-- ----------------------------
-- Table structure for lesson
-- ----------------------------
DROP TABLE IF EXISTS `lesson`;
CREATE TABLE `lesson`  (
  `lesson_id` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `lesson_name` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `credit` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `class_hour` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`lesson_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of lesson
-- ----------------------------
INSERT INTO `lesson` VALUES ('0107', '留学与学术交流应用技能', '2', '16');
INSERT INTO `lesson` VALUES ('0108', '高级英语', '2', '18');
INSERT INTO `lesson` VALUES ('0303', '毛中特', '2', '16');
INSERT INTO `lesson` VALUES ('0911', '人工智能导论', '2.5', '16');
INSERT INTO `lesson` VALUES ('1012', '数据库系统', '3.5', '30');
INSERT INTO `lesson` VALUES ('1017', '算法设计与分析', '3.5', '20');
INSERT INTO `lesson` VALUES ('1023', '软件安全', '2', '16');
INSERT INTO `lesson` VALUES ('1025', '信安数基', '3.5', '20');
INSERT INTO `lesson` VALUES ('1031', '计算机组成原理', '3.5', '20');
INSERT INTO `lesson` VALUES ('1329', '芯片封装', '2', '16');
INSERT INTO `lesson` VALUES ('3001', '网球初级', '1', '16');
INSERT INTO `lesson` VALUES ('3311', '大学物理学（一）', '4', '16');
INSERT INTO `lesson` VALUES ('L002', '操作系统', '3', '48');
INSERT INTO `lesson` VALUES ('L003', '计算机网络', '3', '48');
INSERT INTO `lesson` VALUES ('L004', '数据库原理', '3', '48');
INSERT INTO `lesson` VALUES ('L005', '人工智能导论', '2', '32');
INSERT INTO `lesson` VALUES ('L006', '算法设计与分析', '3', '48');
INSERT INTO `lesson` VALUES ('L007', '软件工程', '3', '48');
INSERT INTO `lesson` VALUES ('L008', '编译原理', '3', '48');
INSERT INTO `lesson` VALUES ('L009', '计算机组成原理', '3', '48');
INSERT INTO `lesson` VALUES ('L010', '现代密码学', '2', '32');
INSERT INTO `lesson` VALUES ('L011', '高等数学', '5', '32');

-- ----------------------------
-- Table structure for major
-- ----------------------------
DROP TABLE IF EXISTS `major`;
CREATE TABLE `major`  (
  `maj_id` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `maj_name` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `col_name` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`maj_id`) USING BTREE,
  INDEX `maj_in_col`(`col_name` ASC) USING BTREE,
  CONSTRAINT `maj_in_col` FOREIGN KEY (`col_name`) REFERENCES `college` (`college_name`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE = InnoDB CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of major
-- ----------------------------
INSERT INTO `major` VALUES ('00001', '信息安全', '网络空间安全学院');
INSERT INTO `major` VALUES ('00002', '软件工程', '软件学院');
INSERT INTO `major` VALUES ('00003', '计算机科学与技术', '计算机学院');
INSERT INTO `major` VALUES ('00004', '光电工程', '电子信息与光学工程学院');
INSERT INTO `major` VALUES ('00005', '自动化科学与技术', '人工智能学院');
INSERT INTO `major` VALUES ('00006', '密码', '网络空间安全学院');
INSERT INTO `major` VALUES ('00007', '软件工程', '软件学院');
INSERT INTO `major` VALUES ('00008', '通信工程', '电子信息与光学工程学院');
INSERT INTO `major` VALUES ('00009', '智能科学与技术', '人工智能学院');

-- ----------------------------
-- Table structure for student
-- ----------------------------
DROP TABLE IF EXISTS `student`;
CREATE TABLE `student`  (
  `stu_id` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `stu_name` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `stu_gender` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `stu_adm_time` date NULL DEFAULT NULL,
  `stu_college` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`stu_id`) USING BTREE,
  UNIQUE INDEX `id_index`(`stu_id` ASC) USING BTREE,
  INDEX `stu_in_col`(`stu_college` ASC) USING BTREE,
  INDEX `stu_name`(`stu_name` ASC) USING BTREE,
  INDEX `stu_adm_time`(`stu_adm_time` ASC) USING BTREE,
  CONSTRAINT `stu_in_col` FOREIGN KEY (`stu_college`) REFERENCES `college` (`college_name`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE = InnoDB CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of student
-- ----------------------------
INSERT INTO `student` VALUES ('00001', '张悦宁', '女', '2020-09-11', '软件学院');
INSERT INTO `student` VALUES ('00002', '王小小', '女', '2020-09-11', '人工智能学院');
INSERT INTO `student` VALUES ('00003', '刘二', '男', '2021-09-13', '计算机学院');
INSERT INTO `student` VALUES ('00006', '李小明', '女', '2022-09-01', '人工智能学院');
INSERT INTO `student` VALUES ('00007', '王大锤', '男', '2021-09-10', '软件学院');
INSERT INTO `student` VALUES ('00008', '赵小红', '女', '2023-09-01', '人工智能学院');
INSERT INTO `student` VALUES ('00009', '钱多多', '女', '2020-09-01', '电子信息与光学工程学院');
INSERT INTO `student` VALUES ('00010', '孙小美', '女', '2022-09-01', '网络空间安全学院');
INSERT INTO `student` VALUES ('00011', '王小小', '女', '2024-05-30', '网络空间安全学院');
INSERT INTO `student` VALUES ('00012', '李二', '女', '2022-09-01', '软件学院');
INSERT INTO `student` VALUES ('00013', '张三', '男', '2021-09-01', '人工智能学院');
INSERT INTO `student` VALUES ('00014', '赵四', '女', '2023-09-01', '电子信息与光学工程学院');
INSERT INTO `student` VALUES ('00015', '王五', '男', '2020-09-01', '网络空间安全学院');
INSERT INTO `student` VALUES ('00016', '李六', '女', '2022-09-01', '计算机学院');
INSERT INTO `student` VALUES ('00017', '陈七', '男', '2021-09-01', '软件学院');
INSERT INTO `student` VALUES ('00018', '张八', '女', '2020-09-01', '人工智能学院');

-- ----------------------------
-- Table structure for student_login
-- ----------------------------
DROP TABLE IF EXISTS `student_login`;
CREATE TABLE `student_login`  (
  `stu_id` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `stu_pwd` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  PRIMARY KEY (`stu_id`) USING BTREE,
  CONSTRAINT `stu_login` FOREIGN KEY (`stu_id`) REFERENCES `student` (`stu_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of student_login
-- ----------------------------
INSERT INTO `student_login` VALUES ('00001', '123456');
INSERT INTO `student_login` VALUES ('00002', '123456');
INSERT INTO `student_login` VALUES ('00003', '123456');
INSERT INTO `student_login` VALUES ('00006', '123456');
INSERT INTO `student_login` VALUES ('00007', '123456');
INSERT INTO `student_login` VALUES ('00008', '123456');
INSERT INTO `student_login` VALUES ('00009', '123456');
INSERT INTO `student_login` VALUES ('00010', '123456');
INSERT INTO `student_login` VALUES ('00011', '123456');
INSERT INTO `student_login` VALUES ('00012', '123456');
INSERT INTO `student_login` VALUES ('00013', '123456');
INSERT INTO `student_login` VALUES ('00014', '123456');
INSERT INTO `student_login` VALUES ('00015', '123456');
INSERT INTO `student_login` VALUES ('00016', '123456');
INSERT INTO `student_login` VALUES ('00017', '123456');
INSERT INTO `student_login` VALUES ('00018', '123456');

-- ----------------------------
-- Table structure for teach
-- ----------------------------
DROP TABLE IF EXISTS `teach`;
CREATE TABLE `teach`  (
  `tea_id` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `lesson_id` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `end_way` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `class` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`tea_id`, `lesson_id`) USING BTREE,
  INDEX `les`(`lesson_id` ASC) USING BTREE,
  INDEX `class`(`class` ASC) USING BTREE,
  CONSTRAINT `les` FOREIGN KEY (`lesson_id`) REFERENCES `lesson` (`lesson_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `tea` FOREIGN KEY (`tea_id`) REFERENCES `teacher` (`tea_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of teach
-- ----------------------------
INSERT INTO `teach` VALUES ('01001', '0107', '开卷', 'C321');
INSERT INTO `teach` VALUES ('01001', '0303', '开卷', 'C321');
INSERT INTO `teach` VALUES ('01001', '0911', '开卷', 'C321');
INSERT INTO `teach` VALUES ('01001', '1012', '开卷', 'C321');
INSERT INTO `teach` VALUES ('01001', '3311', '开卷', 'C321');
INSERT INTO `teach` VALUES ('01001', 'L003', '开卷', 'C321');
INSERT INTO `teach` VALUES ('01001', 'L006', '开卷', 'C321');
INSERT INTO `teach` VALUES ('01008', 'L002', '闭卷考试', 'B309');
INSERT INTO `teach` VALUES ('01009', 'L003', '开卷考试', 'C121');
INSERT INTO `teach` VALUES ('01010', 'L004', '论文', 'C122');
INSERT INTO `teach` VALUES ('01011', 'L005', '展示', 'C123');
INSERT INTO `teach` VALUES ('01016', '0911', '无期末考试', 'D101');
INSERT INTO `teach` VALUES ('01016', '1012', '论文', 'D102');
INSERT INTO `teach` VALUES ('01016', 'L007', '开卷考试', 'D103');
INSERT INTO `teach` VALUES ('01017', '1017', '展示', 'D105');
INSERT INTO `teach` VALUES ('01017', '1023', '闭卷', 'E102');
INSERT INTO `teach` VALUES ('01017', 'L008', '论文', 'E103');
INSERT INTO `teach` VALUES ('01018', '1025', '开卷', 'E105');
INSERT INTO `teach` VALUES ('01018', 'L009', '展示', 'E109');
INSERT INTO `teach` VALUES ('01019', '1031', '无期末考试', 'F102');
INSERT INTO `teach` VALUES ('01019', '1329', '论文', 'F130');
INSERT INTO `teach` VALUES ('01019', 'L010', '闭卷考试', 'F180');
INSERT INTO `teach` VALUES ('01020', '3001', '展示', 'W121');
INSERT INTO `teach` VALUES ('01020', 'L011', '闭卷', 'W131');

-- ----------------------------
-- Table structure for teacher
-- ----------------------------
DROP TABLE IF EXISTS `teacher`;
CREATE TABLE `teacher`  (
  `tea_id` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `tea_name` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `tea_title` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `tea_salary` int NOT NULL,
  `tea_college` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`tea_id`) USING BTREE,
  INDEX `tea_in_col`(`tea_college` ASC) USING BTREE,
  CONSTRAINT `tea_in_col` FOREIGN KEY (`tea_college`) REFERENCES `college` (`college_name`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE = InnoDB CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of teacher
-- ----------------------------
INSERT INTO `teacher` VALUES ('01001', '冯浩', '讲师', 10000, '人工智能学院');
INSERT INTO `teacher` VALUES ('01002', '张伟', '教授', 20000, '计算机学院');
INSERT INTO `teacher` VALUES ('01003', '李娜', '副教授', 18000, '软件学院');
INSERT INTO `teacher` VALUES ('01004', '王强', '讲师', 15000, '网络空间安全学院');
INSERT INTO `teacher` VALUES ('01005', '赵丽', '讲师', 15000, '人工智能学院');
INSERT INTO `teacher` VALUES ('01006', '陈明', '教授', 20000, '电子信息与光学工程学院');
INSERT INTO `teacher` VALUES ('01008', '杨静', '讲师', 15000, '软件学院');
INSERT INTO `teacher` VALUES ('01009', '吴涛', '教授', 20000, '网络空间安全学院');
INSERT INTO `teacher` VALUES ('01010', '孙梅', '副教授', 18000, '人工智能学院');
INSERT INTO `teacher` VALUES ('01011', '胡雷', '讲师', 15000, '电子信息与光学工程学院');
INSERT INTO `teacher` VALUES ('01016', '赵敏', '教授', 32000, '计算机学院');
INSERT INTO `teacher` VALUES ('01017', '李默', '副教授', 28000, '软件学院');
INSERT INTO `teacher` VALUES ('01018', '王辉', '讲师', 18000, '网络空间安全学院');
INSERT INTO `teacher` VALUES ('01019', '周海', '教授', 35000, '电子信息与光学工程学院');
INSERT INTO `teacher` VALUES ('01020', '孙洁', '讲师', 20000, '人工智能学院');

-- ----------------------------
-- Table structure for teacher_login
-- ----------------------------
DROP TABLE IF EXISTS `teacher_login`;
CREATE TABLE `teacher_login`  (
  `tea_id` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `tea_pwd` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  PRIMARY KEY (`tea_id`) USING BTREE,
  CONSTRAINT `tea_login` FOREIGN KEY (`tea_id`) REFERENCES `teacher` (`tea_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of teacher_login
-- ----------------------------
INSERT INTO `teacher_login` VALUES ('01001', '123456');
INSERT INTO `teacher_login` VALUES ('01002', '123456');
INSERT INTO `teacher_login` VALUES ('01003', '123456');
INSERT INTO `teacher_login` VALUES ('01004', '123456');
INSERT INTO `teacher_login` VALUES ('01005', '123456');
INSERT INTO `teacher_login` VALUES ('01006', '123456');
INSERT INTO `teacher_login` VALUES ('01008', '123456');
INSERT INTO `teacher_login` VALUES ('01009', '123456');
INSERT INTO `teacher_login` VALUES ('01010', '123456');
INSERT INTO `teacher_login` VALUES ('01011', '123456');
INSERT INTO `teacher_login` VALUES ('01016', '123456');
INSERT INTO `teacher_login` VALUES ('01017', '123456');
INSERT INTO `teacher_login` VALUES ('01018', '123456');
INSERT INTO `teacher_login` VALUES ('01019', '123456');
INSERT INTO `teacher_login` VALUES ('01020', '123456');

-- ----------------------------
-- View structure for stu_course_info
-- ----------------------------
DROP VIEW IF EXISTS `stu_course_info`;
CREATE ALGORITHM = UNDEFINED SQL SECURITY DEFINER VIEW `stu_course_info` AS select `s`.`stu_id` AS `stu_id`,`s`.`stu_name` AS `stu_name`,`s`.`stu_gender` AS `stu_gender`,`s`.`stu_adm_time` AS `stu_adm_time`,`s`.`stu_college` AS `stu_college`,`le`.`lesson_id` AS `lesson_id`,`le`.`lesson_name` AS `lesson_name`,`le`.`credit` AS `credit`,`le`.`class_hour` AS `class_hour`,`l`.`score` AS `score`,`l`.`class_number` AS `class_number` from ((`student` `s` join `learn` `l` on((`s`.`stu_id` = `l`.`stu_id`))) join `lesson` `le` on((`l`.`lesson_id` = `le`.`lesson_id`)));

-- ----------------------------
-- Procedure structure for delete_student_with_related_records
-- ----------------------------
DROP PROCEDURE IF EXISTS `delete_student_with_related_records`;
delimiter ;;
CREATE PROCEDURE `delete_student_with_related_records`(IN student_id VARCHAR(20))
BEGIN
    DECLARE total_records INT;
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
    END;

    START TRANSACTION;
    DELETE FROM student_login WHERE student_login.stu_id = student_id;
    DELETE FROM learn WHERE learn.stu_id = student_id;
    DELETE FROM student WHERE student.stu_id = student_id;
    SET total_records = (SELECT COUNT(*) FROM student WHERE stu_id = student_id)
                        + (SELECT COUNT(*) FROM student_login WHERE stu_id = student_id)
                        + (SELECT COUNT(*) FROM learn WHERE stu_id = student_id);
    IF total_records = 0 THEN
        COMMIT;
    ELSE
        ROLLBACK;
    END IF;
END
;;
delimiter ;

-- ----------------------------
-- Procedure structure for updata_teach
-- ----------------------------
DROP PROCEDURE IF EXISTS `updata_teach`;
delimiter ;;
CREATE PROCEDURE `updata_teach`(in l varchar(20), in e varchar(255), in c varchar(255), in i varchar(20), in le varchar(20))
BEGIN
    UPDATE lesson 
		SET lesson_id = l 
		WHERE lesson_id = le;
    UPDATE 
		teach SET end_way = e, 
		class = c 
		WHERE tea_id = i;
END
;;
delimiter ;

-- ----------------------------
-- Procedure structure for update_learn_class
-- ----------------------------
DROP PROCEDURE IF EXISTS `update_learn_class`;
delimiter ;;
CREATE PROCEDURE `update_learn_class`()
BEGIN
    DECLARE done INT DEFAULT 0;
    DECLARE stu_id_var VARCHAR(20);
    DECLARE lesson_id_var VARCHAR(20);
    DECLARE class_number_var VARCHAR(20);
    
    -- Declare cursor
    DECLARE cur CURSOR FOR 
        SELECT stu_id, lesson_id FROM learn;

    -- Declare continue handler
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;

    OPEN cur;

    read_loop: LOOP
        FETCH cur INTO stu_id_var, lesson_id_var;
        IF done THEN
            LEAVE read_loop;
        END IF;

        -- Update class_number in learn table based on teach table
        UPDATE learn l
        JOIN teach t ON l.lesson_id = t.lesson_id
        SET l.class_number = t.class
        WHERE l.stu_id = stu_id_var AND l.lesson_id = lesson_id_var;
    END LOOP;

    CLOSE cur;
END
;;
delimiter ;

-- ----------------------------
-- Procedure structure for update_student_major
-- ----------------------------
DROP PROCEDURE IF EXISTS `update_student_major`;
delimiter ;;
CREATE PROCEDURE `update_student_major`(IN student_id VARCHAR(20),
    IN new_col  VARCHAR(255))
BEGIN
    DECLARE avg_score FLOAT;
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = '更新失败：平均分数未达到80分';
    END;
    SELECT AVG(sc.score) INTO avg_score
    FROM learn sc
    WHERE sc.stu_id = student_id;
    IF avg_score >= 80 THEN
        START TRANSACTION;
        UPDATE student
        SET student.stu_college= new_col
        WHERE student.stu_id = student_id;
        COMMIT;
    ELSE
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = '更新失败：平均分数未达到80分';
    END IF;
END
;;
delimiter ;

-- ----------------------------
-- Procedure structure for update_student_score
-- ----------------------------
DROP PROCEDURE IF EXISTS `update_student_score`;
delimiter ;;
CREATE PROCEDURE `update_student_score`(IN student_id VARCHAR(20),
    IN lesson_id VARCHAR(20),
    IN new_score FLOAT)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = '成绩要在0-100分！';
    END;
    START TRANSACTION;
    IF new_score < 0 OR new_score > 100 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = '成绩要在0-100分！';
    ELSE
        UPDATE learn
        SET score = new_score
        WHERE learn.stu_id = student_id AND learn.lesson_id = lesson_id;
    END IF;
    COMMIT;
END
;;
delimiter ;

-- ----------------------------
-- Triggers structure for table learn
-- ----------------------------
DROP TRIGGER IF EXISTS `before_learn_insert`;
delimiter ;;
CREATE TRIGGER `before_learn_insert` BEFORE INSERT ON `learn` FOR EACH ROW BEGIN
    DECLARE total_credits INT;
    SET total_credits = (SELECT SUM(le.credit)
                         FROM learn l
                         JOIN lesson le ON l.lesson_id = le.lesson_id
                         WHERE l.stu_id = NEW.stu_id);
    SET total_credits = total_credits + 
		(SELECT le.credit 
		FROM lesson le 
		WHERE le.lesson_id = NEW.lesson_id);
    -- 检查总学分是否超过 20
    IF total_credits > 20 THEN
        SIGNAL SQLSTATE '45000' 
				SET MESSAGE_TEXT = '学生选课总学分不能超过 20 学分';
    END IF;
END
;;
delimiter ;

-- ----------------------------
-- Triggers structure for table student
-- ----------------------------
DROP TRIGGER IF EXISTS `after_student_insert`;
delimiter ;;
CREATE TRIGGER `after_student_insert` AFTER INSERT ON `student` FOR EACH ROW BEGIN
    INSERT INTO student_login (stu_id, stu_pwd) VALUES (NEW.stu_id, '123456');
END
;;
delimiter ;

-- ----------------------------
-- Triggers structure for table teacher
-- ----------------------------
DROP TRIGGER IF EXISTS `after_teacher_insert`;
delimiter ;;
CREATE TRIGGER `after_teacher_insert` AFTER INSERT ON `teacher` FOR EACH ROW BEGIN
    INSERT INTO teacher_login (tea_id, tea_pwd) VALUES (NEW.tea_id, '123456');
END
;;
delimiter ;

SET FOREIGN_KEY_CHECKS = 1;
