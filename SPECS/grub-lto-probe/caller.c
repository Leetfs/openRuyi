/*
 * SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
 * SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
 * SPDX-License-Identifier: MulanPSL-2.0
 */

int target(void);
int invoke_target(void);

int invoke_target(void)
{
    return target();
}
