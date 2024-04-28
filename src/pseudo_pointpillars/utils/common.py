import os
from box.exceptions import BoxValueError
import yaml
from pseudo_pointpillars import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64

# import torch

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")


@ensure_annotations
def save_json(path: Path, data: dict):
    """save json data

    Args:
        path (Path): path to json file
        data (dict): data to be saved in json file
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logger.info(f"json file saved at: {path}")




@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """load json files data

    Args:
        path (Path): path to json file

    Returns:
        ConfigBox: data as class attributes instead of dict
    """
    with open(path) as f:
        content = json.load(f)

    logger.info(f"json file loaded succesfully from: {path}")
    return ConfigBox(content)


@ensure_annotations
def save_bin(data: Any, path: Path):
    """save binary file

    Args:
        data (Any): data to be saved as binary
        path (Path): path to binary file
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")


@ensure_annotations
def load_bin(path: Path) -> Any:
    """load binary data

    Args:
        path (Path): path to binary file

    Returns:
        Any: object stored in the file
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"


def decodeImage(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close()


def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())
    
# class AverageMeter(object):
#     """Computes and stores the average and current value"""

#     def __init__(self):
#         self.reset()

#     def reset(self):
#         self.val = 0
#         self.avg = 0
#         self.sum = 0
#         self.count = 0

#     def update(self, val, n=1):
#         self.val = val
#         self.sum += val * n
#         self.count += n
#         self.avg = self.sum / self.count


# class Metric(object):
#     def __init__(self):
#         self.RMSELIs = AverageMeter()
#         self.RMSELGs = AverageMeter()
#         self.ABSRs = AverageMeter()
#         self.SQRs = AverageMeter()
#         self.DELTA = AverageMeter()
#         self.DELTASQ = AverageMeter()
#         self.DELTACU = AverageMeter()
#         self.losses = AverageMeter()

#     def update(self, loss, RMSE_Linear, RMSE_Log, abs_relative, sq_relative, delta, delta_sq, delta_cu):
#         if loss:
#             self.losses.update(loss)
#         self.RMSELIs.update(RMSE_Linear)
#         self.RMSELGs.update(RMSE_Log)
#         self.ABSRs.update(abs_relative)
#         self.SQRs.update(sq_relative)
#         self.DELTA.update(delta)
#         self.DELTASQ.update(delta_sq)
#         self.DELTACU.update(delta_cu)

#     def get_info(self):
#         return [self.losses.avg, self.RMSELIs.avg, self.RMSELGs.avg, self.ABSRs.avg, self.SQRs.avg, self.DELTA.avg,
#                 self.DELTASQ.avg, self.DELTACU.avg]

#     def calculate(self, depth, predict, loss=None):
#         # only consider 1~80 meters
#         mask = (depth >= 1) * (depth <= 80)
#         RMSE_Linear = ((((predict[mask] - depth[mask]) ** 2).mean()) ** 0.5).cpu().data
#         RMSE_Log = ((((torch.log(predict[mask]) - torch.log(depth[mask])) ** 2).mean()) ** 0.5).cpu().data
#         abs_relative = (torch.abs(predict[mask] - depth[mask]) / depth[mask]).mean().cpu().data
#         sq_relative = ((predict[mask] - depth[mask]) ** 2 / depth[mask]).mean().cpu().data
#         delta = (torch.max(predict[mask] / depth[mask], depth[mask] / predict[mask]) < 1.25).float().mean().cpu().data
#         delta_sq = (torch.max(predict[mask] / depth[mask],
#                               depth[mask] / predict[mask]) < 1.25 ** 2).float().mean().cpu().data
#         delta_cu = (torch.max(predict[mask] / depth[mask],
#                               depth[mask] / predict[mask]) < 1.25 ** 3).float().mean().cpu().data
#         self.update(loss, RMSE_Linear, RMSE_Log, abs_relative, sq_relative, delta, delta_sq, delta_cu)

#     def tensorboard(self, writer, epoch, token='train'):
#         writer.add_scalar(token + '/RMSELIs', self.RMSELIs.avg, epoch)
#         writer.add_scalar(token + '/RMSELGs', self.RMSELGs.avg, epoch)
#         writer.add_scalar(token + '/ABSRs', self.ABSRs.avg, epoch)
#         writer.add_scalar(token + '/SQRs', self.SQRs.avg, epoch)
#         writer.add_scalar(token + '/DELTA', self.DELTA.avg, epoch)
#         writer.add_scalar(token + '/DELTASQ', self.DELTASQ.avg, epoch)
#         writer.add_scalar(token + '/DELTACU', self.DELTACU.avg, epoch)

#     def print(self, iter, token):
#         string = '{}:{}\tL {:.3f} RLI {:.3f} RLO {:.3f} ABS {:.3f} SQ {:.3f} DEL {:.3f} DELQ {:.3f} DELC {:.3f}'.format(
#             token, iter, *self.get_info())
#         return string


# class Metric1(object):
#     def __init__(self):
#         self.RMSELIs = AverageMeter()
#         self.RMSELGs = AverageMeter()
#         self.ABSRs = AverageMeter()
#         self.SQRs = AverageMeter()
#         self.DELTA = AverageMeter()
#         self.DELTASQ = AverageMeter()
#         self.DELTACU = AverageMeter()
#         self.losses_gt = AverageMeter()
#         self.losses_pseudo = AverageMeter()
#         self.losses_total = AverageMeter()

#     def update(self, loss_gt, loss_pseudo, loss_total, RMSE_Linear, RMSE_Log, abs_relative, sq_relative, delta,
#                delta_sq, delta_cu):
#         self.losses_gt.update(loss_gt)
#         self.losses_pseudo.update(loss_pseudo)
#         self.losses_total.update(loss_total)
#         self.RMSELIs.update(RMSE_Linear)
#         self.RMSELGs.update(RMSE_Log)
#         self.ABSRs.update(abs_relative)
#         self.SQRs.update(sq_relative)
#         self.DELTA.update(delta)
#         self.DELTASQ.update(delta_sq)
#         self.DELTACU.update(delta_cu)

#     def get_info(self):
#         return [self.losses_gt.avg, self.losses_pseudo.avg, self.losses_total.avg, self.RMSELIs.avg, self.RMSELGs.avg,
#                 self.ABSRs.avg, self.SQRs.avg, self.DELTA.avg,
#                 self.DELTASQ.avg, self.DELTACU.avg]

#     def calculate(self, depth, predict, loss_gt=0, loss_psuedo=0, loss_total=0):
#         # only consider 1~80 meters
#         mask = (depth >= 1) * (depth <= 80)
#         RMSE_Linear = ((((predict[mask] - depth[mask]) ** 2).mean()) ** 0.5).cpu().data
#         RMSE_Log = ((((torch.log(predict[mask]) - torch.log(depth[mask])) ** 2).mean()) ** 0.5).cpu().data
#         abs_relative = (torch.abs(predict[mask] - depth[mask]) / depth[mask]).mean().cpu().data
#         sq_relative = ((predict[mask] - depth[mask]) ** 2 / depth[mask]).mean().cpu().data
#         delta = (torch.max(predict[mask] / depth[mask], depth[mask] / predict[mask]) < 1.25).float().mean().cpu().data
#         delta_sq = (torch.max(predict[mask] / depth[mask],
#                               depth[mask] / predict[mask]) < 1.25 ** 2).float().mean().cpu().data
#         delta_cu = (torch.max(predict[mask] / depth[mask],
#                               depth[mask] / predict[mask]) < 1.25 ** 3).float().mean().cpu().data
#         self.update(loss_gt, loss_psuedo, loss_total, RMSE_Linear, RMSE_Log, abs_relative, sq_relative, delta, delta_sq,
#                     delta_cu)

#     def tensorboard(self, writer, epoch, token='train'):
#         writer.add_scalar(token + '/RMSELIs', self.RMSELIs.avg, epoch)
#         writer.add_scalar(token + '/RMSELGs', self.RMSELGs.avg, epoch)
#         writer.add_scalar(token + '/ABSRs', self.ABSRs.avg, epoch)
#         writer.add_scalar(token + '/SQRs', self.SQRs.avg, epoch)
#         writer.add_scalar(token + '/DELTA', self.DELTA.avg, epoch)
#         writer.add_scalar(token + '/DELTASQ', self.DELTASQ.avg, epoch)
#         writer.add_scalar(token + '/DELTACU', self.DELTACU.avg, epoch)

#     def print(self, iter, token):
#         string = '{}:{}\tL {:.3f} {:.3f} {:.3f} RLI {:.3f} RLO {:.3f} ABS {:.3f} SQ {:.3f} DEL {:.3f} DELQ {:.3f} DELC {:.3f}'.format(
#             token, iter, *self.get_info())
#         return string